from django.shortcuts import render,redirect
from .models import TodoModel
from .forms import TodoForm
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    todo_lists = TodoModel.objects.order_by('id')

    form = TodoForm()

    context = {'todo_lists': todo_lists, 'form': form}

    return render(request, 'todo/index.html',context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = TodoModel(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request,task_id):
    todo = TodoModel.objects.get(pk=task_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteTodo(request):

    TodoModel.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):

    TodoModel.objects.all().delete()

    return redirect('index')