#!/usr/bin/env python
"""
Create admin user - hardcoded for reliability
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'picdrop.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Hardcoded values for reliability
username = 'admin'
email = 'admin@picdrop.com'
password = 'picdrop2026'

try:
    user, created = User.objects.get_or_create(
        username=username,
        defaults={'email': email, 'is_staff': True, 'is_superuser': True}
    )
    
    # Always update password
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    
    if created:
        print(f"SUCCESS: Superuser '{username}' created!")
    else:
        print(f"SUCCESS: Superuser '{username}' updated!")
        
except Exception as e:
    print(f"ERROR creating superuser: {e}", file=sys.stderr)
    sys.exit(1)
