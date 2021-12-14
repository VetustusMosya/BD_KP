from django.contrib import admin
from .models import *


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('number', 'brand', 'model', 'driver', 'mechanic')
    # list_editable = ('auto_status',)
    ordering = ('id_auto',)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id_cargo', 'customer', 'pickup_date','pickup_adress','delivery_adress', 'weight', 'type', 'cargo_status')
    list_editable = ('cargo_status',)
    ordering = ('id_cargo',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'adress', 'payment')
    ordering = ('id_customer',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id_delivery', 'cargo', 'car', 'delivery_status')
    list_editable = ('delivery_status',)
    ordering = ('id_delivery',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('f_name', 's_name', 'phone', 'hiring_date')
    # list_editable = ('driver_status',)
    ordering = ('id_driver',)


@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ('f_name', 's_name', 'phone')
    ordering = ('id_mechanic',)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id_storage', 'cargo', 'warehouse', 'storage_status')
    list_editable = ('storage_status',)
    ordering = ('id_storage',)


@admin.register(SupportManager)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('f_name', 's_name', 'phone')
    ordering = ('id_emploee',)


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ('number', 'brand', 'model', 'type', 'volume', 'mechanic')
    # list_editable = ('trailer_status',)
    ordering = ('id_trailer',)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id_place', 'place_status')
    list_editable = ('place_status',)
    ordering = ('id_place',)

# class AutoAdmin(models.ModelAdmin):




