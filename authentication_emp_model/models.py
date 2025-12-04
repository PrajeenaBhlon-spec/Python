from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager




class CustomManager(BaseUserManager):
  def create_user(self , email , username , password , **other_fields):
    email = self.normalize_email(email)
    user = self.model(email = email , username = username , **other_fields)
    user.set_password(password)
    user.save()
    return user
  
  def create_superuser(self , email , username , password , **other_fields):
    other_fields.setdefault("is_staff" , True)
    other_fields.setdefault("is_active" , True)
    other_fields.setdefault("is_superuser" , True)
    if other_fields.get("is_staff") is not True:
      raise ValueError("Superuser must have is_staff=True.")
    if other_fields.get("is_superuser") is not True:
      raise ValueError("Superuser must have is_superuser=True.")
    if other_fields.get("is_active") is not True:
      raise ValueError("Superuser must have is_active = True")
    
    return self.create_user(email , username , password , **other_fields)
  
  

class CustomUser(AbstractBaseUser , PermissionsMixin):
  email = models.CharField(max_length= 100 , unique=True)
  username = models.CharField(max_length=100 , unique=True)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default = False)
  is_superuser = models.BooleanField(default = False)
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username"]

  objects = CustomManager()
  