from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    
    path('food-list/', views.foodList, name="food-list"),
    path('user-list/', views.userList , name="user-list"),
    path('meal-list/', views.mealList, name="meal-list"),
    path('meal-food-list/', views.mealFoodList, name="meal-food-list"),
    
    path('food-detail/<int:pk>/', views.foodDetail, name="food-detail"),
    path('user-detail/<int:pk>/', views.userDetail, name="user-detail"),
    path('meal-detail/<int:pk>/', views.mealDetail, name="meal-detail"),
    
    path('create-food/', views.createFood, name="create-food"),
    path('create-user/', views.createUser, name="create-user"),
    path('create-meal/', views.createMeal, name="create-meal"),
    path('create-meal-food/', views.createMealFood, name="create-meal-food"),
   
   
    path('update-food/<int:pk>/', views.updateFood, name="update-food"),
    path('update-user/<int:pk>/', views.updateUser, name="update-user"),
    path('update-meal/<int:pk>/', views.updateMeal, name="update-meal"),
    
    path('delete-food/<int:pk>/', views.deleteFood, name="delete-food"),
    path('delete-user/<int:pk>/', views.deleteUser, name="delete-user"),
    path('delete-meal/<int:pk>/', views.deleteMeal, name="delete-meal"),
]
