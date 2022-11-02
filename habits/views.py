from django.shortcuts import render
from .models import Habit
# Create your views here.
def list_habits(request):
    habits = Habit.objects.all()
    return render(request, 'list_habits.html',{"habits":habits})
