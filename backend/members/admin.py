from django.contrib import admin
from .models import Member, Payment, Exercise, Health_Metrics

admin.site.register(Member)
admin.site.register(Payment)
admin.site.register(Exercise)
admin.site.register(Health_Metrics)
