from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import datetime

def time_info(request):
    time=datetime.datetime.now()
    s='<h1>Current Date and time is :'+str(time)+'</h1>'
    return HttpResponse(s)
