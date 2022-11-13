from django.urls import path
from api import views as api_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

 path('habits/', api_views.HabitListView.as_view(), name='habit-list-api'),
 #GET REQUEST
 
 path('habits/<int:pk>/', api_views.HabitDetailView.as_view(), name='habit-detail-api'),
 # GET/POST/DELETE REQUEST
 
 path('habits/create/', api_views.HabitCreateView.as_view(), name='habit-create-api'),
 # POST REQUEST
]