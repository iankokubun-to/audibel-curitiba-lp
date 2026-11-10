(() => {
  const id = window.AUDIBEL_CONFIG?.gtmId;
  if (!/^GTM-[A-Z0-9]+$/.test(id || '')) return;
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({'gtm.start': Date.now(), event: 'gtm.js'});
  const script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(id);
  document.head.appendChild(script);
})();
