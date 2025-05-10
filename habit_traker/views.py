from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habit_list.html', {'habits': habits})

def add_habit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        habit = Habit(name=name)
        habit.save()
        return redirect('habit_list')  # Redirect to the habit list after adding a habit

    return render(request, 'add_habit.html')

def view_streak(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)  # Correct way to fetch an object
    return render(request, 'view_streak.html', {'habit': habit})

def mark_done(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)
    habit.streak += 1
    habit.save()
    return redirect('habit_list')

def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)
    habit.delete()
    return redirect('habit_list')
