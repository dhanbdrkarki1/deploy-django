from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm

# Create your views here.
def home(request):
    form = TodoForm()
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'form': form}

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            x = form.cleaned_data['content']
            new_item = Task(content = x)
            new_item.save()
            return redirect('home')
            
    return render(request, 'todolist.html', context)