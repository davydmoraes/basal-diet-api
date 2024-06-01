# Generated by Django 5.0.1 on 2024-06-01 03:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_user_meal_mealuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='foods',
            field=models.ManyToManyField(related_name='meals', through='api.MealFood', to='api.food'),
        ),
        migrations.AddField(
            model_name='mealfood',
            name='amount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='mealfood',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_food', to='api.food'),
        ),
        migrations.AlterField(
            model_name='mealfood',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_food', to='api.meal'),
        ),
    ]
