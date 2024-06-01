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

class MealFoodSerializer(serializers.ModelSerializer):
    food = FoodSerializer()
    class Meta:
        model = MealFood
        fields = ['food', 'amount']

class MealSerializer(serializers.ModelSerializer):
    foods = MealFoodSerializer(source='meal_food', many=True)
    class Meta:
        model = Meal
        fields = ("__all__")

    def create(self, validated_data):
        foods_data = validated_data.pop('meal_food')
        meal = Meal.objects.create(**validated_data)
        for food_data in foods_data:
            food_data_dict = food_data.pop('food')
            food, created = Food.objects.get_or_create(**food_data_dict)
            MealFood.objects.create(meal=meal, food=food, **food_data)
        return meal

    def update(self, instance, validated_data):
        foods_data = validated_data.pop('meal_foods')
        instance.name = validated_data.get('name', instance.name)
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        # Clear old meal foods
        instance.meal_foods.all().delete()

        # Create new meal foods
        for food_data in foods_data:
            food_data_dict = food_data.pop('food')
            food, created = Food.objects.get_or_create(**food_data_dict)
            MealFood.objects.create(meal=instance, food=food, **food_data)

        return instance