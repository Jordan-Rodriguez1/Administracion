from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class address(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_number = models.IntegerField()
    street_numbre = models.IntegerField()
    adrees = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    is_default = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.adrees + ' - by ' + self.id_user.username
