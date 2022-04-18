from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *

# Create your views here.
def index(request):
    context = {'todolist': Todolist.objects.all()}
    return render(request, 'todolist/index.html', context)

def insert(request):
    todo = Todolist(content=request.POST['content'])
    todo.save()
    return redirect('/todolist/')

def delete(request, todo_id):
    todo = Todolist.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todolist/')
    