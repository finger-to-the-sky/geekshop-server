from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    birthday = models.PositiveIntegerField('Age', null=True)


    def safe_delete(self):
        self.is_active = False
        self.save()