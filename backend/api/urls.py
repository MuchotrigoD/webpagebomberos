from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CursoViewSet, NoticiaViewSet, PostulacionViewSet, EfectivoViewSet, VitrinaViewSet,
    login_view, registro_view, me_view, change_password_view
)

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'noticias', NoticiaViewSet)
router.register(r'postulaciones', PostulacionViewSet)
router.register(r'efectivos', EfectivoViewSet)
router.register(r'vitrina', VitrinaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view),
    path('registro/', registro_view),
    path('me/', me_view),
    path('change-password/', change_password_view),
]
