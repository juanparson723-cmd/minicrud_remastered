
// === INICIO DE SESIÓN ===
function login() {
  const user = document.getElementById("loginUser").value.trim();
  const pass = document.getElementById("loginPass").value.trim();

  const usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];
  const encontrado = usuarios.find(u => u.user === user && u.pass === pass);

  if (encontrado) {
    localStorage.setItem("usuarioActivo", user);
    // ¡CAMBIAR ESTO! Redirige a la nueva ruta de Flask
    window.location.href = '/alumnos'; 
  } else {
    alert("Usuario o contraseña incorrectos ❌");
  }
}

// === REGISTRO DE USUARIOS ===
function register() {
  const user = document.getElementById("newUser").value.trim();
  const pass = document.getElementById("newPass").value.trim();

  if (user.length < 5 || pass.length < 6) {
    alert("Usuario mínimo 5 caracteres y contraseña mínimo 6.");
    return;
  }

  const usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];
  const existe = usuarios.find(u => u.user === user);

  if (existe) {
    alert("El usuario ya existe 😅");
    return;
  }

  usuarios.push({ user, pass });
  localStorage.setItem("usuarios", JSON.stringify(usuarios));
  alert("Usuario registrado con éxito ✅");
  window.location.href = "/alumnos";
}

// === LOGOUT ===
function logout() {
  localStorage.removeItem("usuarioActivo");
  window.location.href = '/';
}
