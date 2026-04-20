from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a Bomberos</h1><p>API y administración disponibles en el menú.</p>")
