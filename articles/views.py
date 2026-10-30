from django.shortcuts import render
from django.http.response import HttpResponse
from articles.models import Article, Catalog

# Create your views here.


def hello_world(request):
    return HttpResponse('<h1>hello world<h1>')

def hello_e51an(request):
    return HttpResponse('я @e51an')

def article_list(request: HttpResponse) -> HttpResponse:
    articles = Article.objects.all()
    return HttpResponse(articles)

def catalog_list(request: HttpResponse)-> HttpResponse:
    catalog = Catalog.objects.all()
    return HttpResponse(catalog)