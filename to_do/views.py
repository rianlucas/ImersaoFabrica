from django.shortcuts import render, redirect
from .models import Task, Categoria
from .forms import TaskForm
# Create your views here.

def home(request):
    data = {}
    data['tasks'] = Task.objects.all()
    
    form = TaskForm(request.POST or None)
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')


    return render(request, 'to_do/home.html', data)

def update(request, pk):
    data = {}
    task = Task.objects.get(pk = pk)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('home')

    data['task'] = task
    data['form'] = form
    return render(request, 'to_do/update.html', data)

def delete(request, pk):
    task = Task.objects.get(pk = pk)
    task.delete()
    return redirect('home')