from django.db import models
from .user import User

class Expense(models.Model):
    """Model that represents a product"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10000, decimal_places=2,)
    