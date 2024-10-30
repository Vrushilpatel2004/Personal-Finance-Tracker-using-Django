from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# TYPE = (
#     ('Postive', 'Postive'),
#     ('Negavtive' , 'Negavtive')
#     )

# class Profile(models.Model):
#     user = models.ForeignKey(User , on_delete=models.CASCADE)
#     income = models.FloatField()
#     expenses = models.FloatField(default=0)
#     balance = models.FloatField(blank=True , null=True)
#     list_display =('title',)

# class Expense(models.Model):
#     user = models.ForeignKey(User , on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     amount = models.FloatField()
#     expense_type = models.CharField(max_length=100 , choices=TYPE)
#     list_display =('title',)
    
#     def __str__(self):
#         return self.name
# ----------------------------------------------------------------------------------------

# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models import Sum

# # Define types for expense
# TYPE_CHOICES = (
#     ('Positive', 'Positive'),
#     ('Negative', 'Negative')
# )

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     income = models.FloatField(default=0)
#     balance = models.FloatField(blank=True, null=True)

#     def update_balance(self):
#         # Calculate total expenses associated with the user
#         total_expenses = self.user.expenses.aggregate(total=Sum('amount'))['total'] or 0
#         self.balance = self.income - total_expenses
#         self.save()

# class Expense(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
#     name = models.CharField(max_length=100)
#     amount = models.FloatField()
#     expense_type = models.CharField(max_length=100, choices=TYPE_CHOICES)

#     def __str__(self):
#         return self.name

# ---------------------------------------------------------------------------------------
# from django.db import models
# from django.contrib.auth.models import User

# # Choices for expense type
# TYPE = (
#     ('Positive', 'Positive'),  # Fixed typo here
#     ('Negative', 'Negative'),  # Fixed typo here
# )

# # Profile model to track user's overall income, expenses, and balance
# class Profile(models.Model):
#     # ForeignKey linking to the User model
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     # Fields to track income, expenses, and balance
#     income = models.FloatField()  # Total income
#     expenses = models.FloatField(default=0)  # Total expenses
#     balance = models.FloatField(blank=True, null=True)  # Calculated balance

#     # Display configuration for the admin panel
#     list_display = ('user', 'income', 'expenses', 'balance')

#     def __str__(self):
#         return f"{self.user.username}'s Profile"

#     # Automatically update the balance when income or expenses change
#     def save(self, *args, **kwargs):
#         self.balance = self.income - self.expenses  # Calculate balance
#         super().save(*args, **kwargs)


# # # Expense model to track individual transactions
# class Expense(models.Model):
#     # ForeignKey linking to the User model
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     # Fields to track each transaction
#     name = models.CharField(max_length=100)  # Transaction name
#     amount = models.FloatField()  # Transaction amount
#     expense_type = models.CharField(max_length=100, choices=TYPE)  # Type of transaction (income/expense)

#     # Display configuration for the admin panel
#     list_display = ('name', 'amount', 'expense_type', 'user')

#     def __str__(self):
#         return f"{self.name} - {self.amount} ({self.expense_type})"

#     # Update Profile (balance, income, and expenses) after saving an Expense
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         # Update the user's Profile after adding an expense
#         profile = Profile.objects.get(user=self.user)

#         if self.expense_type == 'Positive':
#             profile.income += self.amount
#         else:
#             profile.expenses += self.amount

#         profile.save()

#     # Automatically adjust the profile when an expense is deleted
#     def delete(self, *args, **kwargs):
#         profile = Profile.objects.get(user=self.user)

#         if self.expense_type == 'Positive':
#             profile.income -= self.amount
#         else:
#             profile.expenses -= self.amount

#         profile.save()
#         super().delete(*args, **kwargs)
# -----------------------------------------------------------------------------

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
