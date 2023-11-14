from django.db import models

# Create your models here.
class carousel(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    estate = models.BooleanField(default=False)
