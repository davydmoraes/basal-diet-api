# Generated by Django 5.0.1 on 2024-06-01 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_meal_foods_mealfood_amount_alter_mealfood_food_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='mealUser',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='basalMetabolicRate',
            new_name='basaletabolic_rate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='selectedGender',
            new_name='selected_gender',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userImage',
            new_name='user_image',
        ),
    ]
