from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event
from photos.models import Photo


def event_list(request):
    """이벤트 목록"""
    events = Event.objects.filter(is_active=True)
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    """이벤트 상세 (관리자 대시보드)"""
    event = get_object_or_404(Event, id=event_id)
    photos = event.photos.all()
    return render(request, 'events/event_detail.html', {
        'event': event,
        'photos': photos
    })


def live_wall(request, event_id):
    """라이브 월 - 실시간 사진 표시"""
    event = get_object_or_404(Event, id=event_id, is_active=True)
    photos = event.photos.all()[:50]  # 최근 50장
    return render(request, 'events/live_wall.html', {
        'event': event,
        'photos': photos
    })


def live_wall_photos(request, event_id):
    """라이브 월 사진 목록 (HTMX polling용)"""
    event = get_object_or_404(Event, id=event_id, is_active=True)
    photos = event.photos.all()[:50]  # 최근 50장
    return render(request, 'events/partials/photo_grid.html', {
        'photos': photos
    })


def delete_photo(request, event_id, photo_id):
    """사진 삭제 (관리자용)"""
    event = get_object_or_404(Event, id=event_id)
    photo = get_object_or_404(Photo, id=photo_id, event=event)
    
    if request.method == 'POST':
        photo.image.delete()  # 파일도 삭제
        photo.delete()
        messages.success(request, '사진이 삭제되었습니다.')
        return redirect('events:event_detail', event_id=event_id)
    
    return render(request, 'events/photo_delete_confirm.html', {
        'event': event,
        'photo': photo
    })
