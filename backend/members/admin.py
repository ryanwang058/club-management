from django.contrib import admin
from .models import Member, Payment, Exercise, Health_Metrics, Fitness_Goals

admin.site.register(Member)
admin.site.register(Payment)
admin.site.register(Exercise)
admin.site.register(Health_Metrics)
admin.site.register(Fitness_Goals)
