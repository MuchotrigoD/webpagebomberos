import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bomberos.settings')
django.setup()

from django.contrib.auth.models import User

emails = ['diegomuchotrigomartinez@gmail.com', 'xanynmisha@gmail.com']

for email in emails:
    try:
        u = User.objects.get(email=email)
        u.is_staff = True
        u.is_superuser = True
        u.save()
        print(f'OK: {email} -> admin/superuser')
    except User.DoesNotExist:
        print(f'NO ENCONTRADO: {email}')
