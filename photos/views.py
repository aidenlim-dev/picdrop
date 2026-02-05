from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from events.models import Event
from .models import Photo


def upload_page(request, event_id):
    """사진 업로드 페이지"""
    event = get_object_or_404(Event, id=event_id, is_active=True)
    return render(request, 'photos/upload.html', {'event': event})


def upload_photo(request, event_id):
    """사진 업로드 처리"""
    event = get_object_or_404(Event, id=event_id, is_active=True)
    
    if request.method == 'POST':
        uploader_name = request.POST.get('uploader_name', '')
        files = request.FILES.getlist('photos')
        
        if not files:
            messages.error(request, '사진을 선택해주세요.')
            return redirect('photos:upload', event_id=event_id)
        
        # 여러 파일 업로드
        uploaded_count = 0
        for file in files:
            Photo.objects.create(
                event=event,
                image=file,
                uploader_name=uploader_name
            )
            uploaded_count += 1
        
        messages.success(request, f'{uploaded_count}장의 사진이 업로드되었습니다!')
        return render(request, 'photos/upload_success.html', {
            'event': event,
            'uploaded_count': uploaded_count
        })
    
    return redirect('photos:upload', event_id=event_id)
