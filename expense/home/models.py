from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    EXPENSE_TYPE_CHOICES = [
        ('Positive', 'Income'),
        ('Negative', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_type = models.CharField(max_length=8, choices=EXPENSE_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.amount}'
