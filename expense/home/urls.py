from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page to show profile and expenses
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),  
    path('expense/',views.expense,name ='expense'),
    path('add/', views.add_expense, name='add_expense'),
    path('update/<int:pk>/', views.update_expense, name='update_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
]
