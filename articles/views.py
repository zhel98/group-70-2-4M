from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from articles.forms import TodoForm
from articles.models import Article, Todo

# Create your views here.



def article_list(request: HttpRequest) -> HttpResponse:
    articles_list = Article.objects.all()
    return render(request,'articles/list.html',{'articles': articles_list})

def article_detail(request: HttpRequest, id: int) -> HttpResponse:
    article = Article.objects.get(id=id)
    return render(request, 'articles/detail.html', {'article': article})


def todo_list(request: HttpRequest) -> HttpResponse:
    todos = Todo.objects.order_by("-created_at", "-pk")
    return render(request, "todos/list.html", {"todos": todos})


def todo_create(request: HttpRequest) -> HttpResponse:
    form = TodoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        todo = form.save()
        return redirect("todo_detail", pk=todo.pk)
    return render(request, "todos/form.html", {"form": form})


def todo_detail(request: HttpRequest, pk: int) -> HttpResponse:
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, "todos/detail.html", {"todo": todo})



def todo_toggle(request: HttpRequest, pk: int) -> HttpResponse:
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save(update_fields=("is_completed",))
    return redirect(reverse("todo_detail", kwargs={"pk": todo.pk}))