from django.db import models


class Auto(models.Model):
    id_auto = models.AutoField(primary_key=True)
    number = models.CharField(unique=True, max_length=9)
    brand = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    oil_type = models.CharField(max_length=7)
    driver = models.ForeignKey('Driver', models.DO_NOTHING)
    mechanic = models.ForeignKey('Mechanic', models.DO_NOTHING)
    # auto_status = models.BooleanField(default=False)

    def __str__(self):
        return self.number

    class Meta:
        managed = False
        db_table = 'auto'
        unique_together = (('id_auto', 'driver', 'mechanic'),)


class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING)
    pickup_date = models.DateField()
    pickup_adress = models.CharField(max_length=45)
    weight = models.IntegerField()
    type = models.CharField(max_length=45)
    cargo_status = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.customer

    class Meta:
        managed = False
        db_table = 'cargo'
        unique_together = (('id_cargo', 'customer'),)


class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    phone = models.IntegerField(unique=True)
    email = models.CharField(unique=True, max_length=45)
    adress = models.CharField(max_length=45)
    contract = models.CharField(unique=True, max_length=9)
    payment = models.IntegerField(blank=True, null=True)
    suporter = models.ForeignKey('SupportManager', models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'customer'
        unique_together = (('id_customer', 'suporter'),)


class Delivery(models.Model):
    id_delivery = models.AutoField(primary_key=True)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    delivery_adress = models.CharField(max_length=45)
    car = models.ForeignKey(Auto, models.DO_NOTHING)
    trailer = models.ForeignKey('Trailer', models.DO_NOTHING)
    delivery_status = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.id_delivery

    class Meta:
        managed = False
        db_table = 'delivery'
        unique_together = (('id_delivery', 'cargo', 'car', 'trailer'),)


class Driver(models.Model):
    id_driver = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=45)
    s_name = models.CharField(max_length=45)
    phone = models.IntegerField(unique=True)
    hiring_date = models.DateField()
    # driver_status = models.BooleanField(default=False)

    def __str__(self):
        return self.s_name

    class Meta:
        managed = False
        db_table = 'driver'


class Mechanic(models.Model):
    id_mechanic = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=45)
    s_name = models.CharField(max_length=45)
    phone = models.IntegerField(unique=True)
    hiring_date = models.DateField()

    def __str__(self):
        return self.s_name

    class Meta:
        managed = False
        db_table = 'mechanic'


class Storage(models.Model):
    id_storage = models.AutoField(primary_key=True)
    cargo = models.ForeignKey('Cargo', models.DO_NOTHING)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING)
    start_date = models.DateField()
    finish_date = models.DateField(blank=True, null=True)
    storage_status = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.id_storage

    class Meta:
        managed = False
        db_table = 'storage'
        unique_together = (('id_storage', 'cargo', 'warehouse'),)


class SupportManager(models.Model):
    id_emploee = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=45)
    s_name = models.CharField(max_length=45)
    phone = models.IntegerField(unique=True)
    hiring_date = models.DateField()

    def __str__(self):
        return self.s_name

    class Meta:
        managed = False
        db_table = 'support_manager'


class Trailer(models.Model):
    id_trailer = models.AutoField(primary_key=True)
    number = models.CharField(unique=True, max_length=9)
    brand = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    volume = models.IntegerField()
    # trailer_status = models.BooleanField(default=False)
    mechanic = models.ForeignKey(Mechanic, models.DO_NOTHING)

    def __str__(self):
        return self.number

    class Meta:
        managed = False
        db_table = 'trailer'
        unique_together = (('id_trailer', 'mechanic'),)


class Warehouse(models.Model):
    id_place = models.AutoField(primary_key=True)
    place_status = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.id_place

    class Meta:
        managed = False
        db_table = 'warehouse'
