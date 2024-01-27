from rest_framework import serializers
from .models import Food, User, Meal, MealFood


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("__all__")
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")
        
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ("__all__")
        
class MealFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealFood
        fields = ("__all__")