from django.db import models
from django.urls import reverse


class Uv(models.Model):
    percent = models.PositiveIntegerField()
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('uv_detail', args=[self.id])
