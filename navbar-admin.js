// navbar-admin.js — Muestra botón "Administrar" en la barra si el usuario es admin/superadmin
(function () {
    const token   = localStorage.getItem('django_token');
    const isAdmin = localStorage.getItem('django_is_admin') === 'true';

    if (!token || !isAdmin) return;

    // Esperar a que el DOM esté listo
    function injectAdminBtn() {
        const menu = document.querySelector('ul.menu');
        if (!menu) return;

        // Evitar duplicados
        if (document.getElementById('nav-admin-btn')) return;

        const li = document.createElement('li');
        li.id = 'nav-admin-btn';

        const a = document.createElement('a');
        a.href = '/admin/';
        a.target = '_blank';
        a.rel = 'noopener';
        a.textContent = 'ADMINISTRAR';
        a.style.cssText = [
            'background:#d32f2f',
            'color:#fff !important',
            'border-radius:6px',
            'padding:6px 14px',
            'font-weight:800',
            'letter-spacing:1px',
            'font-size:0.85em',
            'border:2px solid #b71c1c',
            'transition:background 0.2s',
        ].join(';');

        a.addEventListener('mouseenter', function () {
            this.style.background = '#b71c1c';
        });
        a.addEventListener('mouseleave', function () {
            this.style.background = '#d32f2f';
        });

        li.appendChild(a);

        // Insertar antes del botón LOGIN
        const loginLi = Array.from(menu.querySelectorAll('li')).find(
            li => li.querySelector('a.menu-portal')
        );
        if (loginLi) {
            menu.insertBefore(li, loginLi);
        } else {
            menu.appendChild(li);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', injectAdminBtn);
    } else {
        injectAdminBtn();
    }
})();
