from django.db import models
from .user import User

class Budget(models.Model):
    """Model that represents a category"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10000, decimal_places=2,)
    income = models.DecimalField(max_digits=10000, decimal_places=2,)
