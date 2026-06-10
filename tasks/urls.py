from django.urls import path
from . views import *

urlpatterns = [
    path('', task_list, name="task_list"),
    path('dashboard/', dashboard, name="dashboard"),
    path('add/', add_task, name="add_task"),
    path('edit/<int:id>', edit_task, name="edit_task"),
    path('delete/<int:id>', delete_task, name="delete_task"),
    path('complete/<int:id>', complete_task, name="complete_task"),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name="edit_profile"),
    path('change-password/', change_password, name="change_password"),
    
]