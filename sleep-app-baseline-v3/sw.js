/* Nexus shell. Bump CACHE_VERSION whenever a precached asset changes. */
var CACHE_VERSION = 'nexus-shell-v1';

var SHELL = [
  './index.html',
  './sleep-companion-demo01.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-192.png',
  './icons/icon-maskable-512.png'
];

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_VERSION).then(function (cache) {
      return cache.addAll(SHELL).then(function () {
        return cache.match('./index.html').then(function (index) {
          if (index) return cache.put('./', index);
        });
      });
    }).then(function () {
      return self.skipWaiting();
    })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (key) {
        return key !== CACHE_VERSION;
      }).map(function (key) {
        return caches.delete(key);
      }));
    }).then(function () {
      return self.clients.claim();
    })
  );
});

function isAppHtml(url) {
  return url.pathname.endsWith('/sleep-companion-demo01.html') ||
    url.pathname.endsWith('/index.html') ||
    url.pathname.endsWith('/sleep-app-baseline-v3') ||
    url.pathname.endsWith('/sleep-app-baseline-v3/');
}

self.addEventListener('fetch', function (event) {
  var req = event.request;
  if (req.method !== 'GET') return;
  var url;
  try { url = new URL(req.url); } catch (e) { return; }
  if (url.origin !== self.location.origin) return;

  var accept = req.headers.get('accept') || '';
  var navigation = req.mode === 'navigate' || accept.indexOf('text/html') !== -1;

  if (navigation) {
    event.respondWith(
      fetch(req).then(function (res) {
        if (res && res.ok && isAppHtml(url)) {
          var copy = res.clone();
          caches.open(CACHE_VERSION).then(function (cache) { cache.put(req, copy); });
        }
        return res;
      }).catch(function () {
        return caches.match(req, { ignoreSearch: true }).then(function (hit) {
          if (hit) return hit;
          if (isAppHtml(url)) return caches.match('./sleep-companion-demo01.html');
          return caches.match('./sleep-companion-demo01.html');
        });
      })
    );
    return;
  }

  event.respondWith(
    caches.match(req, { ignoreSearch: true }).then(function (hit) {
      if (hit) return hit;
      return fetch(req).then(function (res) {
        if (res && res.ok) {
          var copy = res.clone();
          caches.open(CACHE_VERSION).then(function (cache) { cache.put(req, copy); });
        }
        return res;
      });
    })
  );
});
