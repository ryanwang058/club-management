# Generated by Django 5.0.3 on 2024-04-02 03:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Health_Metrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bfp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='Fitness_Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
    ]
