#!/usr/bin/env python3
"""
Generate a new Django SECRET_KEY
Usage: python generate_secret_key.py
"""
from django.core.management.utils import get_random_secret_key

if __name__ == '__main__':
    print("New SECRET_KEY for Django:")
    print(get_random_secret_key())
    print("\nAdd this to your Railway environment variables:")
    print(f"SECRET_KEY={get_random_secret_key()}")
