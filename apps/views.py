from django.shortcuts import render, redirect
from django.views import View
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Home(LoginRequiredMixin ,View):
    def get(self , request):
        todos = Todo.objects.filter(user=request.user).order_by('-pk')
        context = {
            "todos":todos,
        }

        return render(request , 'index.html' , context)

    def post(self,request):
        body = request.POST.get('body')
        if body:
            Todo.objects.create(user=request.user , body=body)

        return redirect('home')

class TodoAction(LoginRequiredMixin , View):
    def post(self,request,pk,action):
        todo = Todo.objects.filter(pk=pk , user=request.user).first()
        if todo:
            if action == 'done':
                todo.done = True
                todo.save()
            elif action == 'delete':
                todo.delete()

        return redirect('home')





