# Generated by Django 4.0.3 on 2022-05-02 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodplan', '0002_mealplan_recipes_remove_mealplan_user_mealplan_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mealplan',
            old_name='user',
            new_name='owner',
        ),
    ]
