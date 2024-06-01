from django.urls import path
from .views import MealList, MealDetail, FoodList, FoodDetail, UserList, UserDetail, apiOverview

urlpatterns = [
    path('', apiOverview, name="api-overview"),

    path('food/', FoodList.as_view()),
    path('food/<int:pk>/', FoodDetail.as_view()),
    path('meal/', MealList.as_view()),
    path('meal/<int:pk>/', MealDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]
