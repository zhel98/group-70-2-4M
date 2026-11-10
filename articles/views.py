from django.shortcuts import get_object_or_404, redirect, render

from django.http.response import HttpResponse
from django.http.request import HttpRequest
from articles.forms import CommentForm
from articles.models import Article, Comment

def article_list(request: HttpRequest) -> HttpResponse:
    articles_list = Article.objects.all()
    return render(request,'articles/list.html',{'articles': articles_list})

def article_detail(request: HttpRequest, id: int) -> HttpResponse:
    article = get_object_or_404(Article, id=id)
    comments = Comment.objects.filter(article=article).order_by('created_at')
    return render(request, 'articles/detail.html', {
        'article': article,
        'comments': comments,
        'form': CommentForm(),
    })


def comment_detail(request: HttpRequest, id: int) -> HttpResponse:
    article = get_object_or_404(Article, id=id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('article_detail', id=article.id)

    comments = Comment.objects.filter(article=article).order_by('created_at')
    return render(request, 'articles/detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })