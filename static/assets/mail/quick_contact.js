document.addEventListener('DOMContentLoaded', function() {
  const emailBtn = document.getElementById('contactEmailBtn');
  const modal = document.getElementById('contactEmailModal');
  const closeBtn = document.getElementById('contactModalClose');
  emailBtn.addEventListener('click', () => {
    modal.setAttribute('aria-hidden','false');
    document.body.classList.add('no-scroll');
  });
  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', e => { if(e.target === modal) closeModal(); });
  function closeModal(){
    modal.setAttribute('aria-hidden','true');
    document.body.classList.remove('no-scroll');
  }

  // Envío del formulario
  document.getElementById('quickContactForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const status = document.getElementById('quickContactStatus');
    status.textContent = 'Enviando...';
    const data = new FormData(form);
    try {
      const res = await fetch('static/assets/mail/send_message.php', { // endpoint PHP
        method: 'POST',
        body: data
      });
      let payload = {};
      try { payload = await res.json(); } catch(_) {}
      if(!res.ok || !payload.success){
        const msg = payload.error || 'Error al enviar';
        status.textContent = msg;
        return;
      }
      status.textContent = '¡Mensaje enviado con éxito!';
      form.reset();
      setTimeout(() => {
        const modal = document.getElementById('contactEmailModal');
        modal.setAttribute('aria-hidden','true');
        document.body.classList.remove('no-scroll');
        status.textContent='';
      }, 1500);
    } catch(err){
      status.textContent = 'Error de red';
    }
  });
});