# Generated by Django 5.0.1 on 2024-05-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_meal_mealfood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='selectedGender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Non-Binary')], max_length=1),
        ),
    ]
