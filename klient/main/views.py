from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import Group


def index(request):
    username = request.user.username
    if username == 'worker':
        return render(request, 'main/index.html')
    elif username == 'admin':
        return redirect('admin/')
    else:
        return render(request, 'main/customer.html')


def delivery(request):
    # delivery = Delivery.objects.all()
    delivery = Delivery.objects.raw("select * from delivery")

    return render(request, 'main/delivery.html', {'delivery': delivery})


def storage(request):
    storage = Storage.objects.raw("select * from storage")
    return render(request, 'main/storage.html', {'storage': storage})


def warehouse(request):
    warehouse = Warehouse.objects.raw('call see_empty_place(0);')
    return render(request, 'main/warehouse.html', {'warehouse': warehouse})


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
