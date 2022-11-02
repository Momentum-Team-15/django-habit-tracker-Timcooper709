from django.shortcuts import render
from .models import Habit
# Create your views here.
def list_habit(request):
    habits = Habit.objects.all()
    return render(request, 'list_habit.html',{"habits":habits})
    