from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello_world(request):
    return render(request,'hello.html',{'name':'Anu'})

def hello_jango(request):
    return HttpResponse("<h1>Hello, django. .</h1>")

def hello_python(request):
    return HttpResponse("<h1>Hello, Python. .</h1>")

def add(request):
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    res=val1+val2
    return render(request,'result.html',{'result':res})
