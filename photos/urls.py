from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('<uuid:event_id>/', views.upload_page, name='upload'),
    path('<uuid:event_id>/upload/', views.upload_photo, name='upload_photo'),
]
