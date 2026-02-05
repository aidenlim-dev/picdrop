from django.apps import AppConfig


class EventsConfig(AppConfig):
    name = 'events'
    
    def ready(self):
        # Create superuser on app startup
        import sys
        if 'migrate' not in sys.argv and 'makemigrations' not in sys.argv:
            try:
                from django.contrib.auth import get_user_model
                User = get_user_model()
                if not User.objects.filter(username='admin').exists():
                    User.objects.create_superuser(
                        username='admin',
                        email='admin@picdrop.com',
                        password='picdrop2026'
                    )
                    print("✅ Superuser 'admin' created!")
                else:
                    # Update password
                    user = User.objects.get(username='admin')
                    user.set_password('picdrop2026')
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    print("✅ Superuser 'admin' password updated!")
            except Exception as e:
                print(f"⚠️ Superuser setup: {e}")
