from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo

def home(request):
    return redirect('todo_lists')

def todo_lists(request):
    lists = TodoList.objects.all()
    return render(request, 'todos/todo_lists.html', {'lists': lists})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})

def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')

def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    return render(request, 'todos/edit_todo_list.html', {'todo_list': todo_list})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', id=todo_list_id)

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/edit_todo.html', {'todo': todo})

