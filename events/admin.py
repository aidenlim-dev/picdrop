from django.contrib import admin
from django.utils.html import format_html
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_date', 'is_active', 'photo_count', 'qr_code_preview', 'created_at']
    list_filter = ['is_active', 'event_date']
    search_fields = ['name', 'description']
    readonly_fields = ['id', 'qr_code_preview', 'created_at', 'updated_at', 'upload_link', 'live_wall_link']
    
    fieldsets = (
        ('기본 정보', {
            'fields': ('name', 'description', 'event_date', 'is_active')
        }),
        ('링크', {
            'fields': ('upload_link', 'live_wall_link')
        }),
        ('QR 코드', {
            'fields': ('qr_code', 'qr_code_preview')
        }),
        ('시스템 정보', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def photo_count(self, obj):
        """업로드된 사진 수"""
        count = obj.photos.count()
        return f"{count}장"
    photo_count.short_description = '사진 수'
    
    def qr_code_preview(self, obj):
        """QR 코드 미리보기"""
        if obj.qr_code:
            return format_html(
                '<img src="{}" style="max-width: 200px; max-height: 200px;" />',
                obj.qr_code.url
            )
        return '-'
    qr_code_preview.short_description = 'QR 코드 미리보기'
    
    def upload_link(self, obj):
        """업로드 링크"""
        if obj.id:
            url = f"http://127.0.0.1:8000{obj.get_upload_url()}"
            return format_html(
                '<a href="{}" target="_blank">{}</a>',
                url, url
            )
        return '-'
    upload_link.short_description = '업로드 페이지'
    
    def live_wall_link(self, obj):
        """라이브 월 링크"""
        if obj.id:
            url = f"http://127.0.0.1:8000{obj.get_absolute_url()}"
            return format_html(
                '<a href="{}" target="_blank">{}</a>',
                url, url
            )
        return '-'
    live_wall_link.short_description = '라이브 월'
