from django.db import models
from django.contrib.auth.models import User


class FbModel(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=200)
	feedback = models.TextField()

	def __str__(self):
		return self.name

class CreateModel(models.Model):
	task = models.TextField()
	creation = models.DateTimeField(auto_now_add=True)
	usr = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

	


