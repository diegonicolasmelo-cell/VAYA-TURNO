/* ¡Vaya Turno! — service worker generado por tools/generar_app.py.
   No editar a mano: se rehace con `python3 tools/generar_app.py --pwa`. */
const VERSION = "vt-3069b775ccfe";
const NUCLEO = ["./", "index.html", "manifest.webmanifest", "iconos/icono-192.png", "iconos/icono-512.png", "iconos/icono-maskable-512.png", "iconos/apple-touch-icon.png", "tipos/ArchivoNarrow-500-latin-ext.woff2", "tipos/ArchivoNarrow-500-latin.woff2", "tipos/ArchivoNarrow-600-latin-ext.woff2", "tipos/ArchivoNarrow-600-latin.woff2", "tipos/ArchivoNarrow-700-latin-ext.woff2", "tipos/ArchivoNarrow-700-latin.woff2", "tipos/IBMPlexMono-400-latin-ext.woff2", "tipos/IBMPlexMono-400-latin.woff2", "tipos/IBMPlexMono-500-latin-ext.woff2", "tipos/IBMPlexMono-500-latin.woff2", "tipos/IBMPlexMono-600-latin-ext.woff2", "tipos/IBMPlexMono-600-latin.woff2", "tipos/Petrona-500-latin-ext.woff2", "tipos/Petrona-500-latin.woff2", "tipos/Petrona-500i-latin-ext.woff2", "tipos/Petrona-500i-latin.woff2", "tipos/Petrona-700-latin-ext.woff2", "tipos/Petrona-700-latin.woff2", "tipos/tipos.css"];
const ARTE = ["arte/A01.webp", "arte/A11.webp", "arte/A14.webp", "arte/A19.webp", "arte/C01.webp", "arte/C03.webp", "arte/C05.webp", "arte/C07.webp", "arte/C09.webp", "arte/C11.webp", "arte/C13.webp", "arte/C17.webp", "arte/C19.webp", "arte/C21.webp", "arte/C22.webp", "arte/P02.webp", "arte/P04.webp", "arte/P11.webp", "arte/R07.webp", "arte/R20.webp", "arte/R26.webp", "arte/R30.webp", "arte/R32.webp", "arte/R50.webp", "portada/dibujo.svg", "portada/logo.webp", "portada/portada.jpg", "portada/portada.mp4", "portada/salida.webp"];

self.addEventListener("install", ev => {
  ev.waitUntil((async () => {
    const c = await caches.open(VERSION);
    await c.addAll(NUCLEO);                                  // sin esto no hay app
    await Promise.allSettled(ARTE.map(u => c.add(u)));       // el arte, si se puede
    self.skipWaiting();
  })());
});

self.addEventListener("activate", ev => {
  ev.waitUntil((async () => {
    const viejas = (await caches.keys()).filter(k => k !== VERSION);
    await Promise.all(viejas.map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", ev => {
  const req = ev.request;
  if(req.method !== "GET") return;
  if(req.mode === "navigate"){
    ev.respondWith((async () => {
      try {
        const r = await fetch(req);
        const c = await caches.open(VERSION);
        c.put("index.html", r.clone());
        return r;
      } catch(e) {
        return (await caches.match("index.html")) || Response.error();
      }
    })());
    return;
  }
  ev.respondWith((async () => {
    const hit = await caches.match(req, {ignoreVary: true});
    if(hit) return hit;
    try {
      const r = await fetch(req);
      if(r && (r.ok || r.type === "opaque")){
        const c = await caches.open(VERSION);
        c.put(req, r.clone());
      }
      return r;
    } catch(e) {
      return Response.error();
    }
  })());
});
