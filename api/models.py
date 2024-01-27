from django.db import models

class User(models.Model):
    id = models.SmallIntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField(null=False)
    height = models.DecimalField(decimal_places=2, max_digits=6, null=False)
    weight = models.DecimalField(decimal_places=2, max_digits=6, null=False)
    selectedGender = models.CharField(max_length=6)
    basalMetabolicRate = models.DecimalField(max_digits=6, decimal_places=2)
    userImage = models.ImageField(null=True)
    
    
    def __str__(self):
        return self.name
    
    
class Food(models.Model):
    id = models.SmallIntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=3, max_digits=10, null=False)
    carbohydrates = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    proteins = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    fats = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    calories = models.DecimalField(decimal_places=3, max_digits=10, null=False)
    
    def __str__(self):
        return self.name
    

class Meal(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')

    def __str__(self):
        return self.name
    
class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.meal.name} - {self.food.name}"