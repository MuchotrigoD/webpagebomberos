// Menú 
const menuToggle = document.getElementById('menu-toggle');
const menu = document.querySelector('.menu');

if (menuToggle) {
    menuToggle.addEventListener('change', function() {
        if (this.checked) {
            menu.classList.add('active');
        } else {
            menu.classList.remove('active');
        }
    });
}

// Cerrar menú al hacer clic en un enlace (para móviles)
const menuLinks = document.querySelectorAll('.menu a');
menuLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (menu) {
            menu.classList.remove('active');
        }
        if (menuToggle) {
            menuToggle.checked = false;
        }
    });
});

// Resaltado de enlace activo basado en la URL actual
document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.menu a');

    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});

