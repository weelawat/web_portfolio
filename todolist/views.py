from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *

# Create your views here.
def index(request):

    if request.user.is_authenticated:
        user = request.user
        todolist = Todolist.objects.filter(user=user)
    else:
        todolist = Todolist.objects.filter(user=None)

    context = {'todolist': todolist}
    return render(request, 'todolist/index.html', context)

def insert(request):

    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    
    todo = Todolist(content=request.POST['content'], user=user)
    todo.save()
    return redirect('/todolist/')

def delete(request, todo_id):
    
    todo = Todolist.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todolist/')
    