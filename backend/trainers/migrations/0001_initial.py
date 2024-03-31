# Generated by Django 5.0.3 on 2024-03-30 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('exercise_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer_Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.trainer')),
            ],
        ),
    ]
