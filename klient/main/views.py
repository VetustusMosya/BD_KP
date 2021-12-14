from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import Group


def index(request):
    username = request.user.username
    if username == 'user':
        return render(request,  'main/customer.html')
    else:
        return render(request, 'main/index.html')


def delivery(request):
    delivery = Delivery.objects.all()
    return render(request, 'main/delivery.html', {'delivery': delivery})


def orderDelivery(request):
    error = ''
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Данные не верны'

    form = CargoForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/order_delivery.html', data)

