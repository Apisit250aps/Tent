from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_code = models.CharField(max_length=8, unique=True)
    tel = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=255, unique=True)
    # Address
    address = models.TextField()
    sub_district = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    zip = models.CharField(max_length=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Position(models.Model):
    position_code = models.CharField(max_length=6, unique=True)
    position_name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.position_name}"


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    
    employee_code = models.CharField(max_length=6, unique=True)
    tel = models.CharField(max_length=10)
    
    address = models.TextField()
    sub_district = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    zip = models.CharField(max_length=5)
    
    start_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        
        return f"{self.user.first_name} {self.user.last_name} {self.position.position_name}"
    


class Car(models.Model):
    car_code = models.CharField(max_length=8, unique=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=255)
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.IntegerField(choices=(
        (1, "เตรียมการ"),
        (2, "จอง"),
        (3, "ขายแล้ว")
    ), default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.brand} {self.model} {self.year}"


class Booking(models.Model):
    booking_code = models.CharField(max_length=12, unique=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    pickup_date = models.DateTimeField()
    status = models.IntegerField(choices=(
        (0, "ยกเลิก"),
        (1, "รอชำระ"),
        (2, "จองแล้ว"),
    ), default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.booking_code


class Finance(models.Model):
    finance_code = models.CharField(max_length=12, unique=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    interest_rate = models.FloatField()
    status = models.IntegerField(choices=(
        (0, "ไม่อนุมัติ"),
        (1, "รออนุมัติ"),
        (2, "อนุมัติ"),
    ), default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Period(models.Model):
    period = models.IntegerField()
    finance = models.ForeignKey(Finance, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    pay_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.finance.finance_code} {self.period}"
