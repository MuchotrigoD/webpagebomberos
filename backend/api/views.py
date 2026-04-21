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



# Ahora el registro crea una Postulacion pendiente, no un usuario real
@api_view(['POST'])
@permission_classes([AllowAny])
def registro_view(request):
    nombre       = request.data.get('nombre', '').strip()
    apellido     = request.data.get('apellido', '').strip()
    email        = request.data.get('email', '').strip()
    dni          = request.data.get('dni', '').strip()
    grado        = request.data.get('grado', '').strip()
    descripcion  = request.data.get('descripcion', '').strip()
    fecha_ingreso = request.data.get('fecha_ingreso') or None

    if not nombre or not apellido or not email or not grado:
        return Response({'error': 'Completa todos los campos obligatorios.'}, status=400)
    if Postulacion.objects.filter(email=email, estado='pendiente').exists():
        return Response({'error': 'Ya existe una postulación pendiente con ese correo.'}, status=400)
    # Si ya existe como efectivo, tampoco dejar
    if User.objects.filter(username=email).exists():
        return Response({'error': 'Ya existe una cuenta con ese correo.'}, status=400)

    Postulacion.objects.create(
        nombre=nombre,
        apellido=apellido,
        email=email,
        dni=dni,
        grado_instruccion=grado,
        mensaje=descripcion,
        fecha_nacimiento=None,
        genero='',
        telefono='',
        direccion='',
        distrito='',
        estatura=None,
        peso=None,
        estado='pendiente',
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

    def get_queryset(self):
        qs = super().get_queryset()
        estado = self.request.query_params.get('estado')
        if estado:
            qs = qs.filter(estado=estado)
        return qs

    @action(detail=True, methods=['post'], url_path='aceptar')
    @transaction.atomic
    def aceptar(self, request, pk=None):
        postulacion = self.get_object()
        if postulacion.estado != 'pendiente':
            return Response({'error': 'Ya procesada.'}, status=400)
        # Crear usuario y efectivo
        if User.objects.filter(username=postulacion.email).exists():
            return Response({'error': 'Ya existe un usuario con ese correo.'}, status=400)
        password = get_random_string(12)
        user = User.objects.create_user(
            username=postulacion.email,
            email=postulacion.email,
            password=password,
            first_name=postulacion.nombre,
            last_name=postulacion.apellido
        )
        Efectivo.objects.create(
            user=user,
            dni=postulacion.dni,
            grado=postulacion.grado_instruccion,
            descripcion=postulacion.mensaje,
            fecha_ingreso=None
        )
        postulacion.estado = 'aceptado'
        postulacion.save()
        # Opcional: enviar correo con acceso
        try:
            send_mail(
                'Bienvenido a la Compañía B-120',
                f'Su postulación fue aceptada. Puede ingresar al portal con:\nCorreo: {user.email}\nContraseña: {password}\nhttps://tusitio.com/efectivos.html',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=True
            )
        except Exception:
            pass
        return Response({'ok': True})

    @action(detail=True, methods=['post'], url_path='rechazar')
    def rechazar(self, request, pk=None):
        postulacion = self.get_object()
        if postulacion.estado != 'pendiente':
            return Response({'error': 'Ya procesada.'}, status=400)
        postulacion.estado = 'rechazado'
        postulacion.save()
        return Response({'ok': True})

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
