from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo_realtor = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self) -> str:
        return self.name
