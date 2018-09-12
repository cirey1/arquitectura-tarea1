from django.db import models
from django.utils import timezone

class Comment(models.Model):
    text = models.CharField(max_length=50, null=False)
    comment_date = models.DateTimeField(default=timezone.now, blank=True)
    client_ip = models.CharField(max_length=200)

# Create your models here.
