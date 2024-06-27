document.addEventListener('DOMContentLoaded', (event) => {
  function validarFormulario(event) {
      event.preventDefault()

      var nombreInput = document.getElementById('nombre');
      var correoInput = document.getElementById('correo');
      var celularInput = document.getElementById('celular');
      var ocupacionInput = document.getElementById('ocupacion');

      var nombreError = document.getElementById('nombreError');
      var correoError = document.getElementById('correoError');
      var celularError = document.getElementById('celularError');
      var ocupacionError = document.getElementById('ocupacionError');

      var nombre = nombreInput.value.trim();
      var correo = correoInput.value.trim();
      var celular = celularInput.value.trim();
      var ocupacion = ocupacionInput.value.trim();

      if (nombre === '') {
        event.preventDefault();
        nombreInput.classList.add('invalid');
        nombreInput.classList.remove('valid');
        nombreError.textContent = 'El nombre es requerido';
        return;
    } else if (nombre.length < 3) {
        event.preventDefault();
        nombreInput.classList.add('invalid');
        nombreInput.classList.remove('valid');
        nombreError.textContent = 'El nombre debe tener al menos 3 caracteres';
        return;
    } else {
        nombreInput.classList.add('valid');
        nombreInput.classList.remove('invalid');
        nombreError.textContent = '';
    }

    var correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (correo === '') {
        event.preventDefault();
        correoInput.classList.add('invalid');
        correoInput.classList.remove('valid');
        correoError.textContent = 'El correo electrónico es requerido';
        return;
    } else if (!correoRegex.test(correo)) {
        event.preventDefault();
        correoInput.classList.add('invalid');
        correoInput.classList.remove('valid');
        correoError.textContent = 'El correo electrónico debe ser válido';
        return;
    } else {
        correoInput.classList.add('valid');
        correoInput.classList.remove('invalid');
        correoError.textContent = '';
    }

    var celularRegex = /^\d+$/;
    if (celular === '') {
        event.preventDefault();
        celularInput.classList.add('invalid');
        celularInput.classList.remove('valid');
        celularError.textContent = 'El número de celular es requerido';
        return;
    } else if (!celularRegex.test(celular)) {
        event.preventDefault();
        celularInput.classList.add('invalid');
        celularInput.classList.remove('valid');
        celularError.textContent = 'El número de celular debe ser solo números';
        return;
    } else {
        celularInput.classList.add('valid');
        celularInput.classList.remove('invalid');
        celularError.textContent = '';
    }

    if (ocupacion === '') {
      event.preventDefault();
      ocupacionInput.classList.add('invalid');
      ocupacionInput.classList.remove('valid');
      ocupacionError.textContent = 'La ocupación es requerida';
      return;
  } else if (ocupacion.length < 20) {
      event.preventDefault();
      ocupacionInput.classList.add('invalid');
      ocupacionInput.classList.remove('valid');
      ocupacionError.textContent = 'La ocupación debe tener al menos 20 caracteres';
      return;
  } else {
      ocupacionInput.classList.add('valid');
      ocupacionInput.classList.remove('invalid');
      ocupacionError.textContent = '';
  }
  
    event.target.submit();

    alert('Su solicitud ha sido enviada con éxito');
}

var form = document.getElementById('job-application-form');
form.addEventListener('submit', validarFormulario);
});