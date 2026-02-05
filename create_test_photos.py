#!/usr/bin/env python
"""테스트 사진 생성 스크립트"""
import os
import django
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'picdrop.settings')
django.setup()

from events.models import Event
from photos.models import Photo

# 첫 번째 이벤트 가져오기
event = Event.objects.first()

if not event:
    print("❌ 이벤트가 없습니다. 먼저 create_test_event.py를 실행하세요.")
    exit(1)

# 간단한 테스트 이미지 생성 (컬러풀한 사각형들)
colors = [
    ('#FF6B6B', '빨강'),
    ('#4ECDC4', '청록'),
    ('#45B7D1', '파랑'),
    ('#F7DC6F', '노랑'),
    ('#BB8FCE', '보라'),
]

print(f"📷 테스트 사진 생성 중...")
print(f"   이벤트: {event.name}")

for i, (color, name) in enumerate(colors, 1):
    # 800x600 이미지 생성
    img = Image.new('RGB', (800, 600), color)
    
    # BytesIO로 변환
    buffer = BytesIO()
    img.save(buffer, format='JPEG', quality=85)
    buffer.seek(0)
    
    # InMemoryUploadedFile 생성
    file = InMemoryUploadedFile(
        buffer,
        None,
        f'test_photo_{i}.jpg',
        'image/jpeg',
        buffer.getbuffer().nbytes,
        None
    )
    
    # Photo 생성
    photo = Photo.objects.create(
        event=event,
        image=file,
        uploader_name=f'테스터{i}'
    )
    
    print(f"   ✅ 사진 {i}/{len(colors)} 생성: {name} ({photo.id})")

print(f"\n✅ 총 {len(colors)}장의 테스트 사진이 업로드되었습니다!")
print(f"   - 라이브 월에서 확인: http://127.0.0.1:8000{event.get_absolute_url()}")
print(f"   - 관리자 대시보드: http://127.0.0.1:8000/events/{event.id}/")
