from django.contrib import admin

from habit_traker.models import Habit
from django.shortcuts import render 

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'streak', 'last_marked_date')
    search_fields = ('name',)
