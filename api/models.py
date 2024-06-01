from django.db import models

class User(models.Model):
    GENDER_CHOICES = (
        ("F", "Female"),
        ("M", "Male"),
        ("I", "Intersex")
    )

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=False)
    height = models.DecimalField(decimal_places=2, max_digits=6, null=False)
    weight = models.DecimalField(decimal_places=2, max_digits=6, null=False)
    selected_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, null=False)
    basal_metabolic_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    user_image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name


class Food(models.Model):
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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meals")
    foods = models.ManyToManyField(Food, related_name="meals", through="MealFood")


    def __str__(self):
        return self.name

class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="meal_food")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="meal_food")
    amount = models.DecimalField(decimal_places=3, max_digits=10, null=False, default=0)

    def __str__(self):
        return f"{self.meal.name} - {self.food.name}"