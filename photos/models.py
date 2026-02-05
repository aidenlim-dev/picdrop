from django.db import models
from events.models import Event
import uuid


class Photo(models.Model):
    """사진 모델"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos', verbose_name='이벤트')
    image = models.ImageField('사진', upload_to='photos/%Y/%m/%d/')
    uploaded_at = models.DateTimeField('업로드 시간', auto_now_add=True)
    uploader_name = models.CharField('업로더 이름', max_length=100, blank=True)
    
    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = '사진'
        verbose_name_plural = '사진'
    
    def __str__(self):
        return f"{self.event.name} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"
    
    @property
    def thumbnail_url(self):
        """썸네일 URL (실제로는 원본 사용, 나중에 최적화 가능)"""
        return self.image.url if self.image else ''
