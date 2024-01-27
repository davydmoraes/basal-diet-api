from django.urls import path
from .views import FoodList, FoodDetail, UserList, UserDetail, MealList, MealDetail, MealFoodList, MealFoodDetail

urlpatterns = [
    path('food/', FoodList.as_view()),
    path('food/<int:pk>/', FoodDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('meal/', MealList.as_view()),
    path('meal/<int:pk>', MealDetail.as_view()),
    path('meal-food/', MealFoodList.as_view()),
    path('meal-food/<int:pk>', MealFoodDetail.as_view()),

]
