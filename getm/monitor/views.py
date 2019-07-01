from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request, "monitor/index.html")

def register (request):
    return render(request, "monitor/register.html")

def registered (request):
    return HttpResponse("TBD")

def searching (request):
    return HttpResponse("search page")