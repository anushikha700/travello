from django.shortcuts import render

# Create your views here.

def destination(request):
    return render(request,'destination.html')
