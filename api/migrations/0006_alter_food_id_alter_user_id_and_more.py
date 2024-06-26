# Generated by Django 5.0.1 on 2024-05-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_food_options_alter_meal_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='selectedGender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('I', 'Intersex')], max_length=1),
        ),
    ]
