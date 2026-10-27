from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def hello_world(request):
    return HttpResponse('<h1>hello world<h1>')

def hello_e51an(request):
    return HttpResponse('я @e51an')