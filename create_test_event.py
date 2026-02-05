#!/usr/bin/env python
"""테스트 이벤트 생성 스크립트"""
import os
import django
from datetime import date

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'picdrop.settings')
django.setup()

from events.models import Event

# 테스트 이벤트 생성
event = Event.objects.create(
    name='테스트 웨딩 파티',
    description='행복한 순간을 함께 공유해요! 사진을 업로드해주세요.',
    event_date=date.today(),
    is_active=True
)

print(f"✅ 이벤트 생성 완료!")
print(f"   - ID: {event.id}")
print(f"   - 이름: {event.name}")
print(f"   - QR 코드: {event.qr_code.url if event.qr_code else '생성 안됨'}")
print(f"   - 업로드 URL: http://127.0.0.1:8000{event.get_upload_url()}")
print(f"   - 라이브 월 URL: http://127.0.0.1:8000{event.get_absolute_url()}")
