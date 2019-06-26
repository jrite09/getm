from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, "monitor/index.html")

def searching (request):
    return render(request, "monitor/index.html")