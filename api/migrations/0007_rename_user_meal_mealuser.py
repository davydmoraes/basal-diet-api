# Generated by Django 5.0.1 on 2024-05-30 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_food_id_alter_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='user',
            new_name='mealUser',
        ),
    ]
