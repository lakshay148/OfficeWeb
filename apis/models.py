from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=256, default='')
    email = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    role = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Module(models.Model):
    """Module Table"""

    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20)


class Domain(models.Model):
    """Module Table"""

    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20)


class Privilige(models.Model):
    """Privilige Table"""

    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20)


class Role(models.Model):
    """Role Table"""

    name = models.CharField(max_length=40)
    pid = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20)


class Task(models.Model):
    """Task Table"""

    name = models.CharField(max_length=40)
    module = models.IntegerField()
    domain = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField()
    created_by = models.CharField(max_length=20)
