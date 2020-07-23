from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dests= Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

def destination(request):
    dest_id=request.GET.get('dest_id')
    dest= Destination.objects.get(pk=dest_id)
    return render(request,'destination.html',{'dest':dest})
