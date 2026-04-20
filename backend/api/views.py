from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Curso, Noticia, Postulacion, Efectivo, Vitrina
from .serializers import CursoSerializer, NoticiaSerializer, PostulacionSerializer, EfectivoSerializer, VitrinaSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'is_admin': user.is_staff or user.is_superuser})
    return Response({'error': 'Credenciales incorrectas'}, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def registro_view(request):
    nombre       = request.data.get('nombre', '').strip()
    apellido     = request.data.get('apellido', '').strip()
    email        = request.data.get('email', '').strip()
    password     = request.data.get('password', '')
    dni          = request.data.get('dni', '').strip()
    grado        = request.data.get('grado', '').strip()
    descripcion  = request.data.get('descripcion', '').strip()
    fecha_ingreso = request.data.get('fecha_ingreso') or None

    if not nombre or not apellido or not email or not password or not grado:
        return Response({'error': 'Completa todos los campos obligatorios.'}, status=400)
    if len(password) < 10:
        return Response({'error': 'La contraseña debe tener al menos 10 caracteres.'}, status=400)
    if User.objects.filter(username=email).exists():
        return Response({'error': 'Ya existe una cuenta con ese correo.'}, status=400)

    user = User.objects.create_user(
        username=email, email=email, password=password,
        first_name=nombre, last_name=apellido
    )
    Efectivo.objects.create(
        user=user, dni=dni, grado=grado,
        descripcion=descripcion, fecha_ingreso=fecha_ingreso
    )
    return Response({'ok': True})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    user = request.user
    data = {
        'username':  user.username,
        'email':     user.email,
        'nombre':    user.first_name,
        'apellido':  user.last_name,
        'is_admin':  user.is_staff or user.is_superuser,
    }
    try:
        ef = user.efectivo
        data.update({
            'dni':          ef.dni,
            'grado':        ef.grado,
            'descripcion':  ef.descripcion,
            'fecha_ingreso': str(ef.fecha_ingreso) if ef.fecha_ingreso else '',
            'foto_url':     ef.foto_url,
        })
    except Efectivo.DoesNotExist:
        pass
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password_view(request):
    new_pass = request.data.get('new_password', '')
    if len(new_pass) < 6:
        return Response({'error': 'La contraseña debe tener al menos 6 caracteres.'}, status=400)
    user = request.user
    user.set_password(new_pass)
    user.save()
    Token.objects.filter(user=user).delete()
    token = Token.objects.create(user=user)
    return Response({'token': token.key})

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('-creado_en')
    serializer_class = CursoSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all().order_by('-fecha')
    serializer_class = NoticiaSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

class PostulacionViewSet(viewsets.ModelViewSet):
    queryset = Postulacion.objects.all().order_by('-fecha')
    serializer_class = PostulacionSerializer
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

class EfectivoViewSet(viewsets.ModelViewSet):
    queryset = Efectivo.objects.select_related('user').all()
    serializer_class = EfectivoSerializer
    permission_classes = [permissions.IsAdminUser]


class VitrinaViewSet(viewsets.ModelViewSet):
    queryset = Vitrina.objects.all().order_by('orden')
    serializer_class = VitrinaSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
