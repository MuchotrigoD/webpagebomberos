from rest_framework import serializers
from .models import Curso, Noticia, Postulacion, Efectivo, Vitrina

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

class PostulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = '__all__'
        read_only_fields = ('fecha',)

class EfectivoSerializer(serializers.ModelSerializer):
    nombre   = serializers.SerializerMethodField()
    apellido = serializers.SerializerMethodField()
    email    = serializers.SerializerMethodField()
    is_staff = serializers.SerializerMethodField()

    class Meta:
        model  = Efectivo
        fields = ['id', 'nombre', 'apellido', 'email', 'is_staff',
                  'dni', 'grado', 'descripcion', 'fecha_ingreso', 'foto_url']

    def get_nombre(self, obj):   return obj.user.first_name
    def get_apellido(self, obj): return obj.user.last_name
    def get_email(self, obj):    return obj.user.email
    def get_is_staff(self, obj): return obj.user.is_staff or obj.user.is_superuser


class VitrinaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Vitrina
        fields = '__all__'
