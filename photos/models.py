from django.db import models

# these two lines can be remove, nothing will change
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Photo(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) # can be remove, nothing will change
    img = models.ImageField(default='default-image.jpg', upload_to='photos')
    title = models.CharField(max_length=64)
    date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title