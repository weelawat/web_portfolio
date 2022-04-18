from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]