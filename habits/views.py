from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from .models import Habit, DateRecord
from .forms import HabitForm, DateRecordForm

# Create your views here.
def list_habit(request):
    habits = Habit.objects.all()
    return render(request, 'list_habit.html',{"habits":habits})

def create_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to='create_habit')

    return render(request, "create_habit.html", {"form":form})


def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    daterecords = DateRecord.objects.filter(habit=habit)
    context = {"habit": habit, "daterecords": daterecords}
    if request.method == "GET":
        form = DateRecordForm()
    else:
        form = DateRecordForm(data=request.POST)
        if form.is_valid():
            daterecord = form.save(commit=False)
            daterecord.habit = habit
            try:
                daterecord.save()
            except IntegrityError as error:
                context["error_msg"] = "A record already exits for this date."
    context["form"] = form
    return render(request, "habit_detail.html", context)

def delete_habit(request,pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method =="POST":
        habit.delete()
        return redirect(to = "list_habit")

    return render(request, "delete_habit.html", {"habit":habit})   

def edit_habit(request,pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
     form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect (to='list_habit')

    return render(request, "edit_habit.html", {"form":form, "habit":habit})




