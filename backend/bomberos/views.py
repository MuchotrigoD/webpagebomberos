from pathlib import Path
from django.views.static import serve as static_serve

FRONTEND_DIR = Path(__file__).resolve().parent.parent.parent

def home(request):
    return static_serve(request, 'index.html', document_root=FRONTEND_DIR)

def serve_page(request, filename):
    return static_serve(request, filename, document_root=FRONTEND_DIR)
