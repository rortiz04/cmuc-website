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
      const res = await fetch('/send_message', {
        method: 'POST',
        body: data
      });
      if(!res.ok) throw new Error('Error');
      status.textContent = '¡Mensaje enviado con éxito! Nos pondremos en contacto pronto.';
      form.reset();
      setTimeout(closeModal, 1200);
    } catch(err){
      status.textContent = 'Error al enviar';
    }
  });
});