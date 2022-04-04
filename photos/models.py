from django.db import models
# from django.contrib.auth.models import User

from django.conf import settings
User = settings.AUTH_USER_MODEL

class Photo(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    img = models.ImageField(default='default-image.jpg', upload_to='photos')
    title = models.CharField(max_length=99)
    date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title