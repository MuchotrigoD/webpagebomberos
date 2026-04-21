from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CursoViewSet, NoticiaViewSet, PostulacionViewSet, EfectivoViewSet, VitrinaViewSet,
    login_view, registro_view, me_view, change_password_view
)
schema_view = get_schema_view(
    openapi.Info(
        title="API Bomberos",
        default_version='v1',
        description="Documentación interactiva de la API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'noticias', NoticiaViewSet)
router.register(r'postulaciones', PostulacionViewSet)
router.register(r'efectivos', EfectivoViewSet)
router.register(r'vitrina', VitrinaViewSet)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('login/', login_view),
    path('registro/', registro_view),
    path('me/', me_view),
    path('change-password/', change_password_view),
]
