from django.shortcuts import render
from django.http import HttpResponse
from .models import Auto


def index(request):
    return render(request, 'main/index.html')

# def (request):
#     return render(request, 'main/index.html')
