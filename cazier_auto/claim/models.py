from django.db import models
from django.contrib.auth.models import User


class Claim(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    series = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
