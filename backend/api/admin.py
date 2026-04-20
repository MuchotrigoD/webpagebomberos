from django.contrib import admin
from .models import Curso, Noticia, Postulacion, Efectivo, Vitrina

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'tipo', 'creado_en')
    list_filter   = ('tipo',)
    search_fields = ('titulo', 'descripcion')
    ordering      = ('-creado_en',)
    list_per_page = 20

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'etiqueta', 'fecha', 'creado_en')
    list_filter   = ('etiqueta',)
    search_fields = ('titulo', 'descripcion')
    ordering      = ('-fecha',)
    list_per_page = 20

@admin.register(Postulacion)
class PostulacionAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'apellido', 'dni', 'email', 'telefono', 'estado', 'fecha')
    list_filter   = ('estado',)
    search_fields = ('nombre', 'apellido', 'email', 'dni')
    ordering      = ('-fecha',)
    list_per_page = 20
    readonly_fields = ('fecha',)

@admin.register(Efectivo)
class EfectivoAdmin(admin.ModelAdmin):
    list_display  = ('__str__', 'grado', 'dni', 'fecha_ingreso')
    list_filter   = ('grado',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'dni')
    ordering      = ('grado',)
    list_per_page = 20

@admin.register(Vitrina)
class VitrinaAdmin(admin.ModelAdmin):
    list_display  = ('cargo', 'nombre', 'orden', 'creado_en')
    search_fields = ('cargo', 'nombre')
    ordering      = ('orden',)
    list_per_page = 20
