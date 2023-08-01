from django.db import models

class User(models.Model):
    """Model that represents a rare user"""
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    uid = models.CharField(max_length=10000)
