# Generated by Django 5.0.3 on 2024-04-02 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
