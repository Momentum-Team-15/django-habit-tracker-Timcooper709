"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from habits import views 
from api import views as api_views


urlpatterns = [
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("accounts/logout/",views.log_out, name ='log_out'),


    path('', views.list_habit, name="list_habit"),
    path('habits/add/', views.create_habit, name="create_habit"),
    path('habits/<int:pk>/', views.habit_detail, name="habit_detail"),
    path('habits/<int:pk>/delete', views.delete_habit, name="delete_habit"), 
    path('habits/<int:pk>/edit',views.edit_habit, name="edit_habit"), 
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include("api.urls"))

]
