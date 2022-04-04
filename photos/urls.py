from django.urls import path
from photos import views

app_name = 'photos'

urlpatterns = [
    path('photos/', views.photos_view, name='photos'),
    path('photos/add', views.add_photo, name='add_photo'),
]