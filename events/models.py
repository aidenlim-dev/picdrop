from django.db import models
from django.utils import timezone
import uuid
import qrcode
from io import BytesIO
from django.core.files import File


class Event(models.Model):
    """이벤트 모델"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('이벤트 이름', max_length=200)
    description = models.TextField('설명', blank=True)
    event_date = models.DateField('이벤트 날짜')
    created_at = models.DateTimeField('생성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    qr_code = models.ImageField('QR 코드', upload_to='qrcodes/', blank=True)
    is_active = models.BooleanField('활성화', default=True)
    
    class Meta:
        ordering = ['-event_date']
        verbose_name = '이벤트'
        verbose_name_plural = '이벤트'
    
    def __str__(self):
        return self.name
    
    def get_upload_url(self):
        """업로드 URL 반환"""
        from django.urls import reverse
        return reverse('photos:upload', kwargs={'event_id': self.id})
    
    def get_absolute_url(self):
        """라이브 월 URL 반환"""
        from django.urls import reverse
        return reverse('events:live_wall', kwargs={'event_id': self.id})
    
    def generate_qr_code(self):
        """QR 코드 생성"""
        # 업로드 URL 생성 (절대 URL)
        upload_url = f"http://127.0.0.1:8000{self.get_upload_url()}"
        
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(upload_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 이미지를 BytesIO에 저장
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        
        # 파일로 저장
        filename = f'qr_{self.id}.png'
        self.qr_code.save(filename, File(buffer), save=False)
        buffer.close()
    
    def save(self, *args, **kwargs):
        """저장 시 QR 코드 자동 생성"""
        is_new = self._state.adding
        super().save(*args, **kwargs)
        
        # 새로 생성되거나 QR 코드가 없으면 생성
        if is_new or not self.qr_code:
            self.generate_qr_code()
            super().save(update_fields=['qr_code'])
