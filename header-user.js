// Script global para mostrar las iniciales del usuario logueado en el header en todas las vistas
// Oculta el botón LOGIN por defecto para evitar parpadeo
var style = document.createElement('style');
style.innerHTML = '.menu-portal { visibility: hidden !important; } .menu-portal.ready { visibility: visible !important; }';
document.head.appendChild(style);

(function() {
    function isLoggedIn() {
        return !!localStorage.getItem('django_token');
    }
    function updateHeaderUser() {
        var menuPortal = document.querySelector('.menu-portal');
        if (!menuPortal) return;
        if (isLoggedIn()) {
            var initials = '';
            try {
                var nombre = localStorage.getItem('user_nombre') || '';
                var apellido = localStorage.getItem('user_apellido') || '';
                initials = ((nombre[0] || '') + (apellido[0] || '')).toUpperCase() || '?';
            } catch { initials = '?'; }
            menuPortal.textContent = initials;
            menuPortal.classList.add('user-initials');
            menuPortal.href = 'efectivos.html';
            menuPortal.onclick = function(e) {
                // Si ya estamos en efectivos.html, cerrar sesión; si no, solo navegar
                if (window.location.pathname.endsWith('efectivos.html')) {
                    e.preventDefault();
                    localStorage.removeItem('django_token');
                    localStorage.removeItem('django_is_admin');
                    localStorage.removeItem('user_nombre');
                    localStorage.removeItem('user_apellido');
                    menuPortal.textContent = 'LOGIN';
                    menuPortal.classList.remove('user-initials');
                    menuPortal.href = 'efectivos.html';
                    menuPortal.onclick = null;
                    menuPortal.title = '';
                    window.location.href = 'efectivos.html';
                } // Si no, solo deja el comportamiento normal (redirigir)
            };
            menuPortal.title = 'Ir a portal de efectivos o cerrar sesión';
        } else {
            menuPortal.textContent = 'LOGIN';
            menuPortal.classList.remove('user-initials');
            menuPortal.href = 'efectivos.html';
            menuPortal.onclick = null;
            menuPortal.title = '';
        }
        menuPortal.classList.add('ready');
    }
    document.addEventListener('DOMContentLoaded', updateHeaderUser);
    window.addEventListener('storage', updateHeaderUser);
})();