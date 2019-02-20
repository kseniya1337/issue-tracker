import random
import uuid

import requests
from django.contrib.auth.models import AbstractUser
from django.core.files.base import ContentFile
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
        verbose_name='аватар',
    )

    def __str__(self):
        return self.get_full_name() or self.username

    def save(self, *args, **kwargs):
        if not self.avatar:
            response = requests.get('https://ui-avatars.com/api/', params={
                'name': str(self),
                'background': hex(int(random.random() * 0xFFFFFF))[-6:].upper(),
                'size': 256,
            })
            self.avatar.save(str(uuid.uuid4()) + '.png', ContentFile(response.content))
        super().save(*args, **kwargs)