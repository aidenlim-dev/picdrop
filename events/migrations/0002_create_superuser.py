from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create(
            username='admin',
            email='admin@picdrop.com',
            password=make_password('picdrop2026'),
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        print("Superuser 'admin' created via migration!")
    else:
        # Update existing user
        user = User.objects.get(username='admin')
        user.password = make_password('picdrop2026')
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        print("Superuser 'admin' updated via migration!")


def reverse_func(apps, schema_editor):
    pass  # Don't delete on reverse


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_func),
    ]
