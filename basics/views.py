from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Todo


def index(request):
    todo_items = Todo.objects.all()
    context = {
        'todos': todo_items,
    }
    return render(request, 'todo-items.html', context)


def mark_done(request, todo_id):
    todo_item = get_object_or_404(Todo, id=todo_id)
    todo_item.mark_as_done()
    return HttpResponse()


def mark_not_done(request, todo_id):
    todo_item = get_object_or_404(Todo, id=todo_id)
    todo_item.mark_as_not_done()
    return HttpResponse()
