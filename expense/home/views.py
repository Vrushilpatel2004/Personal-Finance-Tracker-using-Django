from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.success(request, f'Welcome, {user.username}!')
                return redirect('expense')  # Redirect to the homepage after successful login
            # else:
            #     messages.error(request, 'Invalid username or password.')
      #  else:
         #   messages.error(request, 'Invalid username or password.')
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'home/login.html', {})

def custom_logout(request):
    # Perform logout
    logout(request)
    
    # Optional: Add a success message for feedback
   # messages.success(request, "You have been successfully logged out.")
    
    # Render the custom logout page
    return render(request, 'home/logout.html')
    
# ------------------------------------------------------------------------------------------------------------------
def home(request):
    return render(request, 'home/welcome.html', {})
# ----------------------------------------------------------------------------------------------------------------------
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def expense(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-created_at')
    income = expenses.filter(expense_type='Positive').aggregate(total=models.Sum('amount'))['total'] or 0
    expense = expenses.filter(expense_type='Negative').aggregate(total=models.Sum('amount'))['total'] or 0
    balance = income - expense
    user_name = request.user.username
    context = {
        'user_name': user_name,
        'expenses': expenses,
        'profile': {
            'income': income,
            'expenses': expense,
            'balance': balance,
        }
    }
    return render(request, 'expense.html', context)

@login_required(login_url='/login/')
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

@login_required(login_url='/login/')
def update_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'update_expense.html', {'form': form})

@login_required(login_url='/login/')
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense')
    return render(request, 'delete_expense.html', {'expense': expense})
