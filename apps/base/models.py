from django.db import models
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class CustomUser(AbstractUser):
    """ Custom User Model """

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class ImageDrop(models.Model):
    """ Dropzone image """
    image = ProcessedImageField(upload_to='images/',
                                processors=[ResizeToFill(300, 300)],
                                format='PNG',
                                options={'quality': 80}
                                )


    def __str__(self):
        return str(self.image.name)