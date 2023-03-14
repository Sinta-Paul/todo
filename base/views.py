from django.shortcuts import render,redirect
from .models import Task

def home(request):
    task=Task.objects.all()
    context={'tasks_created':task,'task_count':task.count}
    return render(request,'base/main.html',context)

def createtask(request):
    tasks=Task.objects.create(
            task=request.POST.get('task_body')
        )
    context={'tasks':tasks}
    return redirect('home')

def deletetask(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('home')
