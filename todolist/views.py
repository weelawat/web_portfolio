from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Todopage(View):

    items = ["Buy food", "Learn coding"]

    def get(self, request):
        
        return render(request, 'todolist/todo_page.html', {'items': self.items})

    def post(self, request):

        newitem = request.POST["newitem"]
        self.items.append(newitem)
        return render(request, 'todolist/todo_page.html', {'items': self.items})
    
    