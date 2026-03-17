/*File che attiva la PWA, caricato in ogni pagina tramite base.html
serve a dire al browser di registrare il Service Worker per l'applicazione
*/
window.onload = () => {
    'use strict';

    if ('serviceWorker' in navigator) {
        navigator.serviceWorker
            .register('/sw.js').then(function (registration) {
                    // Service worker registered correctly.
                console.log('ServiceWorker registration successful with scope: ', registration.scope);
                },
            function (err) {

                // Troubles in registering the service worker. :(
                console.log('ServiceWorker registration failed: ', err);
            });
    }
}