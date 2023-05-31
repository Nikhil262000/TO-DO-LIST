from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser

class ProfileModel(models.Model):
	added_by = models.ForeignKey(User, on_delete = models.CASCADE)
	lo = models.CharField(max_length=20) 
	eo = models.CharField(max_length=20,null=True) 

class MyUser(AbstractBaseUser):
	username = models.CharField(max_length=20,primary_key=True) 
	email = models.CharField(max_length=20)

	USERNAME_FIELD = 'username'
