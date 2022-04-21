# Generated by Django 4.0.3 on 2022-04-21 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0006_step_food_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('recipes', models.ManyToManyField(related_name='tags', to='recipes.recipe')),
            ],
        ),
    ]
