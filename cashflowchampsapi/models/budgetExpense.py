from django.db import models
from .expense import Expense
from .budget import Budget

class BudgetExpense(models.Model):
    """Model that represents a post tag"""
    expense_id = models.ForeignKey(Expense, on_delete=models.CASCADE)
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE)
