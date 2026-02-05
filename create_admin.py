#!/usr/bin/env python
"""
Run this script to create/update admin user.
Usage: python create_admin.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'picdrop.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@picdrop.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'picdrop2026')

user, created = User.objects.get_or_create(
    username=username,
    defaults={'email': email, 'is_staff': True, 'is_superuser': True}
)

if created:
    user.set_password(password)
    user.save()
    print(f"Superuser '{username}' created successfully!")
else:
    # Update password even if user exists
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"Superuser '{username}' password updated!")
