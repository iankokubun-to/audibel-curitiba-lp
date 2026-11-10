(() => {
  const config = window.AUDIBEL_CONFIG || {};
  const phone = String(config.whatsapp || '').replace(/\D/g, '');
  const buttons = document.querySelectorAll('[data-whatsapp]');
  const dialog = document.querySelector('.preview-dialog');
  if (/^55\d{10,11}$/.test(phone)) {
    const url = new URL(`https://wa.me/${phone}`);
    url.searchParams.set('text', config.message || 'Olá! Quero participar da Lista VIP da Black Friday Audibel.');
    buttons.forEach(button => {
      button.href = url.href;
      button.target = '_blank';
      button.rel = 'noopener noreferrer';
      button.addEventListener('click', () => {
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({event: 'click_wpp', event_category: 'conversion', cta_name: button.dataset.cta, destination: 'whatsapp', city: config.citySlug.replace(/-/g, '_')});
      });
    });
  } else {
    buttons.forEach(button => button.addEventListener('click', event => {
      event.preventDefault();
      dialog.showModal();
    }));
  }
  dialog.querySelectorAll('button').forEach(button => button.addEventListener('click', () => dialog.close()));
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
})();
