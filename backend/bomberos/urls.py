
from django.contrib import admin
from django.urls import path, include, re_path
from .views import home, serve_page

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^(?P<filename>[\w\-\.]+\.(html|css|js|json|png|jpg|jpeg|gif|svg|ico|webp|woff|woff2|ttf))$', serve_page, name='serve_page'),
]
