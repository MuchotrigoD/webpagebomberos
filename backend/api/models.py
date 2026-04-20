from django.db import models

class Curso(models.Model):
    TIPO_CHOICES = [
        ('Curso', 'Curso'),
        ('Manual', 'Manual'),
        ('Documento', 'Documento'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='Curso')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    url = models.URLField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    etiqueta = models.CharField(max_length=50, blank=True)
    imagen_url = models.URLField(blank=True, max_length=500)
    media_urls = models.JSONField(default=list, blank=True)
    youtube_url = models.URLField(blank=True, max_length=500)
    fecha = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha']


class Postulacion(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    distrito = models.CharField(max_length=100, blank=True)
    estatura = models.IntegerField(null=True, blank=True)
    peso = models.IntegerField(null=True, blank=True)
    grado_instruccion = models.CharField(max_length=50, blank=True)
    mensaje = models.TextField(blank=True)
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado'), ('rechazado', 'Rechazado')],
        default='pendiente'
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"

    class Meta:
        verbose_name = 'Postulación'
        verbose_name_plural = 'Postulaciones'
        ordering = ['-fecha']


class Efectivo(models.Model):
    GRADO_CHOICES = [
        ('Brigadier', 'Brigadier'),
        ('Ten. Brigadier', 'Ten. Brigadier'),
        ('Capitán', 'Capitán'),
        ('Teniente', 'Teniente'),
        ('Sub Teniente', 'Sub Teniente'),
        ('Seccionario', 'Seccionario'),
        ('Aspirante', 'Aspirante'),
        ('Postulante', 'Postulante'),
    ]
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='efectivo')
    dni = models.CharField(max_length=20, blank=True)
    grado = models.CharField(max_length=50, choices=GRADO_CHOICES, blank=True)
    descripcion = models.TextField(blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    foto_url = models.URLField(blank=True, max_length=500)

    def __str__(self):
        return f"{self.user.get_full_name()} — {self.grado}"

    class Meta:
        verbose_name = 'Efectivo'
        verbose_name_plural = 'Efectivos'


class Vitrina(models.Model):
    cargo        = models.CharField(max_length=100)
    nombre       = models.CharField(max_length=150, blank=True)
    descripcion  = models.TextField(blank=True)
    fecha_ingreso = models.CharField(max_length=30, blank=True)
    foto_url     = models.URLField(blank=True, max_length=500)
    orden        = models.IntegerField(default=9999)
    creado_en    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cargo} — {self.nombre}"

    class Meta:
        verbose_name = 'Vitrina'
        verbose_name_plural = 'Vitrina'
        ordering = ['orden']
