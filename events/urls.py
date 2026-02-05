from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<uuid:event_id>/', views.event_detail, name='event_detail'),
    path('<uuid:event_id>/live/', views.live_wall, name='live_wall'),
    path('<uuid:event_id>/live/photos/', views.live_wall_photos, name='live_wall_photos'),
    path('<uuid:event_id>/photos/<uuid:photo_id>/delete/', views.delete_photo, name='delete_photo'),
]
