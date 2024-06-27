document.addEventListener('DOMContentLoaded', (event) => {
function validarCotizacion(event) {
    console.log('Validando cotización')
    var seleccionInput = document.getElementById('seleccion');
    var nombreInput = document.getElementById('nombre');
    var mensajeInput = document.getElementById('mensaje');
    var telefonoInput = document.getElementById('telefono');
    var correoInput = document.getElementById('correo');

    var seleccion = seleccionInput.value.trim();
    var nombre = nombreInput.value.trim();
    var mensaje = mensajeInput.value.trim();
    var telefono = telefonoInput.value.trim();
    var correo = correoInput.value.trim();

    if (nombre === '') {
        event.preventDefault();
        nombreInput.classList.add('invalid');
        nombreInput.classList.remove('valid');
        nombreError.textContent = 'El nombre de la tarea es requerido';
        return;
    } else if (nombre.length < 5) {
        event.preventDefault();
        nombreInput.classList.add('invalid');
        nombreInput.classList.remove('valid');
        nombreError.textContent = 'El nombre de la tarea debe tener al menos 5 caracteres';
        return;
    } else {
        nombreInput.classList.add('valid');
        nombreInput.classList.remove('invalid');
        nombreError.textContent = '';
    }

    if (mensaje === '' || mensaje.length < 20) {
        event.preventDefault();
        mensajeInput.classList.add('invalid');
        mensajeInput.classList.remove('valid');
        mensajeError.textContent = 'El detalle de la tarea es requerido y debe tener al menos 20 caracteres';
        return;
    } else {
        mensajeInput.classList.add('valid');
        mensajeInput.classList.remove('invalid');
        mensajeError.textContent = '';
    }

    var telefonoRegex = /^\d+$/;
    if (telefono === '' || !telefonoRegex.test(telefono)) {
        event.preventDefault();
        telefonoInput.classList.add('invalid');
        telefonoInput.classList.remove('valid');
        telefonoError.textContent = 'El número de teléfono es requerido y debe ser solo números';
        return;
    } else {
        telefonoInput.classList.add('valid');
        telefonoInput.classList.remove('invalid');
        telefonoError.textContent = '';
    }

    var correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (correo === '' || !correoRegex.test(correo)) {
        event.preventDefault();
        correoInput.classList.add('invalid');
        correoInput.classList.remove('valid');
        correoError.textContent = 'El correo electrónico es requerido y debe ser válido';
        return;
    } else {
        correoInput.classList.add('valid');
        correoInput.classList.remove('invalid');
        correoError.textContent = '';
    }

    event.target.submit();

    alert('Su cotización ha sido enviada con éxito');
}

var form = document.getElementById('cotizacion-form');
form.addEventListener('submit', validarCotizacion);
});