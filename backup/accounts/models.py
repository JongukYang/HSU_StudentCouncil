from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    # username, password, email 등 몇가지 필드는 
    # django.contrib.auth.models User 모델에 이미 존재함
    realName = models.CharField(max_length=20, null=True, blank=True)