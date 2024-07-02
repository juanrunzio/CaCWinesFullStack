//--------------Juan--------------------------------
// Selecciona el menú hamburguesa
const menuIcon = document.getElementById("menu");

// Añade un evento de clic al menú hamburguesa
menuIcon.addEventListener("click", function () {
  // Alternar la clase 'menu-open' en el elemento header
  document.querySelector(".header").classList.toggle("menu-open");
});

//--------------------------------------------------
// Area de Facundo JS Validacion de Forms

document.addEventListener("DOMContentLoaded", function() {
  const form = document.querySelector("form");

  form.addEventListener("submit", function(event) {
      // Obtener los valores de los campos
      const nombre = document.getElementById('nombre').value.trim();
      const apellido = document.getElementById('apellido').value.trim();
      const correo = document.getElementById('correo').value.trim();
      const telefono = document.getElementById('telefono').value.trim();
      
      // Valida que este completo el form
      if (nombre === '') {
          alert('Por favor, ingrese su nombre.');
          event.preventDefault();
          return;
      }

      if (apellido === '') {
          alert('Por favor, ingrese su apellido.');
          event.preventDefault();
          return;
      }

      // Valida correo
      // Solo que tenga el @
      const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!regexCorreo.test(correo)) {
          alert('Por favor, ingrese un correo electrónico válido.');
          event.preventDefault();
          return;
      }

      // Valida el Celular (Por numeros y Largo)
      // Solo por numero de 10 digitos
      const regexTelefono = /^[0-9]{10}$/; 
      if (!regexTelefono.test(telefono)) {
          alert('Por favor, ingrese un número de teléfono válido de 10 dígitos.');
          event.preventDefault();
          return;
      }

      
  });
});





//--------------------------------------------------