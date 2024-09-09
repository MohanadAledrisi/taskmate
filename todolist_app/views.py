from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context={
        
    }
    return render(request,"index.html",context)

@login_required
def todolist(request):
    if request.method== "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save()
        messages.success(request,("New Task Added!"))
        return redirect("todolist")
    else:
        all_task = Task.objects.filter(owner=request.user)
        paginator= Paginator(all_task,3)
        page= request.GET.get('pg')
        all_task=paginator.get_page(page)
        context ={
            "all_tasks":all_task,
            "welcome":'Welcome to do list app'
        }
        return render(request,"todolist.html",context)
    
@login_required
def delete_task(request,task_id):
    
    task = Task.objects.get(pk=task_id)
    if task.owner==request.user:
        task.delete()
    else:
        messages.error(request,("Access Restrected! You are not allowed"))

    return redirect("todolist")

@login_required
def edit_task(request,task_id):
    if request.method== "POST":
        task = Task.objects.get(pk=task_id)
        form = TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Edited Task Successfully!"))
        return redirect("todolist")
    else:
        task_obj = Task.objects.get(pk=task_id)
        context ={
            "task_obj":task_obj,
            "welcome":'Welcome to Edit Page'
        }
        return render(request,"edit.html",context)
    
@login_required
def complete_task(request,task_id):
    task=Task.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done= True
        task.save()
    else:
        messages.error(request,("Access Restrected! You are not allowed"))

    return redirect("todolist")
@login_required

def pending_task(request,task_id):
    task=Task.objects.get(pk=task_id)
    if task.owner==request.user:
        task.done= False
        task.save()
    else:
        messages.error(request,("Access Restrected! You are not allowed"))

    return redirect("todolist")

def contact(request):
    context ={
        "welcome":'Welcome contact app'
    }
    return render(request,"contact.html",context)
def about(request):
    context ={
        "welcome":'Welcome to about app'
    }
    return render(request,"about.html",context)