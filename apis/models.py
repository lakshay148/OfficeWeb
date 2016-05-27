from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=40)
	password = models.CharField(max_length=256,default='')
	email = models.CharField(max_length=100,default='')
	phone = models.IntegerField(default=0)
	role = models.IntegerField(default=0)
