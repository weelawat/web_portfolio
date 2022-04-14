from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.Todopage.as_view(), name="todo_page"),
]