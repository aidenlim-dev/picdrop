from django.contrib import admin
from django.utils.html import format_html
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_preview', 'event', 'uploader_name', 'uploaded_at']
    list_filter = ['event', 'uploaded_at']
    search_fields = ['event__name', 'uploader_name']
    readonly_fields = ['id', 'uploaded_at', 'image_preview']
    
    fieldsets = (
        ('기본 정보', {
            'fields': ('event', 'uploader_name')
        }),
        ('사진', {
            'fields': ('image', 'image_preview')
        }),
        ('시스템 정보', {
            'fields': ('id', 'uploaded_at'),
            'classes': ('collapse',)
        }),
    )
    
    def thumbnail_preview(self, obj):
        """썸네일 미리보기 (리스트용)"""
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />',
                obj.image.url
            )
        return '-'
    thumbnail_preview.short_description = '미리보기'
    
    def image_preview(self, obj):
        """이미지 미리보기 (상세 페이지용)"""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 500px; max-height: 500px;" />',
                obj.image.url
            )
        return '-'
    image_preview.short_description = '이미지 미리보기'
