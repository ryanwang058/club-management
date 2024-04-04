"""
URL configuration for club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registration URL
    path('register/', views.register, name='register'),

    # Account URL
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),

    # dashboard URL
    path('dashboard/', views.dashboard_dispatcher, name='dashboard_dispatcher'),
    path('dashboard/member/', views.member_dashboard, name='member_dashboard'),
    path('dashboard/trainer/', views.trainer_dashboard, name='trainer_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),

    # Other apps including members, trainers, rooms
    path('members/', include('members.urls')),
    path('trainers/', include('trainers.urls')),
    path('adminstaff/', include('adminstaff.urls'))
]
