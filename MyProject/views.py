from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('this is home')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('this is about')
    return render(request, 'about.html')