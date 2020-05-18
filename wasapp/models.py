from django.conf import settings
from django.db import models
from django.utils import timezone


class waitingperson(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=2)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()