from django.db import models
from django.conf import settings
# Create your models here.
class Employee(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , null=True)
  name = models.CharField(max_length=100)
  address = models.CharField(max_length= 50)
  empType = models.CharField(max_length=50)
  salary = models.IntegerField()

  def __str__(self):
    return self.user.username 