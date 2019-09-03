from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class CustomUser(AbstractUser):
    self_description = models.TextField(blank=True, null=False, default='')
    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='user_images')

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)
