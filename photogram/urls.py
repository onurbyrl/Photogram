from django.contrib import admin
from django.urls import path, include
from users import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('photos.urls')),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)