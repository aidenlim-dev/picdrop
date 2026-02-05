#!/usr/bin/env python3
"""
Check if the project is ready for deployment
Usage: python check_deployment.py
"""
import os
import sys

def check_files():
    """Check if all required files exist"""
    required_files = [
        'requirements.txt',
        'Procfile',
        'railway.json',
        'runtime.txt',
        '.gitignore',
        'manage.py',
        'picdrop/settings.py',
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print("❌ Missing required files:")
        for f in missing:
            print(f"   - {f}")
        return False
    else:
        print("✅ All required files present")
        return True

def check_settings():
    """Check settings.py for production readiness"""
    with open('picdrop/settings.py', 'r') as f:
        content = f.read()
    
    checks = {
        'Environment variables': 'os.environ.get' in content,
        'Database config': 'dj_database_url' in content,
        'Whitenoise middleware': 'whitenoise' in content,
        'Cloudinary storage': 'cloudinary' in content,
        'Security settings': 'SECURE_SSL_REDIRECT' in content,
    }
    
    all_passed = True
    for check_name, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"{status} {check_name}")
        if not passed:
            all_passed = False
    
    return all_passed

def check_git():
    """Check if git is initialized"""
    if os.path.exists('.git'):
        print("✅ Git repository initialized")
        return True
    else:
        print("❌ Git not initialized")
        print("   Run: git init && git add . && git commit -m 'Initial commit'")
        return False

def main():
    print("🚀 PicDrop Deployment Readiness Check\n")
    print("=" * 50)
    
    print("\n📁 File Check:")
    files_ok = check_files()
    
    print("\n⚙️  Settings Check:")
    settings_ok = check_settings()
    
    print("\n🔄 Git Check:")
    git_ok = check_git()
    
    print("\n" + "=" * 50)
    
    if files_ok and settings_ok and git_ok:
        print("\n✅ Project is ready for deployment!")
        print("\n📋 Next steps:")
        print("1. Sign up at https://railway.app")
        print("2. Sign up at https://cloudinary.com")
        print("3. Follow QUICK_DEPLOY.md")
        return 0
    else:
        print("\n❌ Project is NOT ready for deployment")
        print("Please fix the issues above")
        return 1

if __name__ == '__main__':
    sys.exit(main())
