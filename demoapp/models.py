from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)

class userlogin(models.Model):
    user = models.ForeignKey(Login,on_delete = models.CASCADE,related_name = 'user',null=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    age = models.IntegerField(null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    address = models.TextField(max_length=150)
    image = models.ImageField()

    def __str__(self):
        return self.name

class addevent(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name
