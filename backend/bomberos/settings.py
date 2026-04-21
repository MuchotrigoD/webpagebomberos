import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
INSTALLED_APPS = [
    # ...otras apps...
    'rest_framework',
    'drf_yasg',
    # ...otras apps...
]
# Forzar encoding UTF-8 para la conexión con PostgreSQL en Windows
os.environ['PGCLIENTENCODING'] = 'UTF8'
os.environ['LANG'] = 'en_US.UTF-8'

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'cambia-esta-clave-en-produccion')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'drf_yasg',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bomberos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bomberos.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'bomberosdb'),
        'USER': os.getenv('POSTGRES_USER', 'bomberosuser'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'Navigate3434'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
        'OPTIONS': {
            'client_encoding': 'UTF8',
            'options': '-c lc_messages=C -c client_encoding=UTF8',
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS: permite que el frontend HTML consulte al backend
CORS_ALLOW_ALL_ORIGINS = DEBUG  # En desarrollo permite todo; en producción restringe

JAZZMIN_SETTINGS = {
    "site_title": "B-120 Admin",
    "site_header": "Bomberos B-120",
    "site_brand": "B-120",
    "site_logo": None,
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Panel de Administración — Compañía de Bomberos B-120",
    "copyright": "© Compañía de Bomberos B-120",
    "search_model": ["api.Curso", "api.Noticia", "api.Postulacion", "api.Efectivo", "api.Vitrina"],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Panel", "url": "admin:index"},
        {"name": "Ver Sitio Web", "url": "/", "new_window": True},
        {"name": "Noticias", "url": "/noticias.html", "new_window": True},
        {"name": "Postulaciones", "url": "/postulaciones.html", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "Ver Sitio", "url": "/", "new_window": True, "icon": "fas fa-globe"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "api",
        "api.Noticia",
        "api.Curso",
        "api.Postulacion",
        "api.Efectivo",
        "api.Vitrina",
        "auth",
    ],
    "icons": {
        "auth": "fas fa-shield-alt",
        "auth.user": "fas fa-user-circle",
        "auth.Group": "fas fa-users",
        "api": "fas fa-fire",
        "api.Curso": "fas fa-graduation-cap",
        "api.Noticia": "fas fa-newspaper",
        "api.Postulacion": "fas fa-file-signature",
        "api.Efectivo": "fas fa-id-badge",
        "api.Vitrina": "fas fa-star",
    },
    "default_icon_parents": "fas fa-fire-extinguisher",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-danger",
    "accent": "accent-danger",
    "navbar": "navbar-danger navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-danger",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cosmo",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": True,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
