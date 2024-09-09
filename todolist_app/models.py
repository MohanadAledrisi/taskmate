from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Task(models.Model):
    task= models.CharField(max_length=30)
    done= models.BooleanField(default=False)
    owner =models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__(self) -> str:
        return str(self.owner)