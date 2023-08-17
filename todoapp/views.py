from django.shortcuts import render, redirect, HttpResponse
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = { 
               'tasks': tasks
                }
    return render(request, 'index.html', context)
    
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if title and description:
            Task.objects.create(title=title, description=description)
            return redirect('index')
        
        else:
            context = {
                'error': 'Title and Description is required'
            }
        return render(request, 'create.html', context)
    
    return render(request, 'create.html')

def delete(request, id):
    
    task = Task.objects.get(id=id)
    task.delete()

    return redirect('index')
    
def edit(request, id):
    task = Task.objects.get(id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        task.title = title
        task.description = description    
 
        task.save()
        return redirect('index')
        
    context = {
        'task': task
    }
    
    return render(request, 'edit.html', context)

def mark_completed(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()
    
    return redirect('index')