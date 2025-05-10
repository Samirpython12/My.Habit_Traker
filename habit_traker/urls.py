from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('habit_list/', views.habit_list, name='habit_list'),
    path('add_habit/', views.add_habit, name='add_habit'),
    path('mark_done/<int:habit_id>/', views.mark_done, name='mark_done'),
    path('view_streak/<int:habit_id>/', views.view_streak, name='view_streak'),
    path('delete_habit/<int:habit_id>/', views.delete_habit, name='delete_habit'),

]
