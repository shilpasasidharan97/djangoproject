from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('welcome')

def index(request):
    return render(request,'index.html')
def html(request):
    return render(request,'html.html')
def css(request):
    return render(request,'css.html')
def java(request):
    return render(request,'js.html')