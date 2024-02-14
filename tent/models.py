from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CAR_STATUS = (
    (1, "Ready"),
    (2, "Reserved"),
    (3, "Sold")
)

RESERVATION_STATUS = (
    (1, "Reserved"),
    (2, "Pending"),
    (3, "Cancelled")
)

PAYMENT_METHOD = (
    (1, "Cash"),
    (2, "Bank")
)

FINANCE_STATUS = (
    (1, "Pending"),
    (2, "Approved"),
    (3, "Rejected"),
)

SALE_STATUS = (
    (1, "Pending"),
    (2, "Paid")
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_code = models.CharField(max_length=8, unique=True)
    tel = models.CharField(max_length=10, unique=True, null=False)
    email = models.CharField(max_length=255, unique=True, null=True)
    credit_info = models.TextField(null=True)
    # Address
    address = models.TextField(default=True)
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
    position_name = models.CharField(max_length=255, null=False)
    description = models.TextField(default="-")

    def __str__(self):
        return f"{self.position_name}"


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    # Contact
    employee_code = models.CharField(max_length=6, unique=True)
    tel = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=255, unique=True, null=True)
    # Address
    address = models.TextField()
    sub_district = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    zip = models.CharField(max_length=5)
    #
    start_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.user.first_name} {self.user.last_name} {self.position.position_name}"


class Car(models.Model):
    car_code = models.CharField(max_length=8, unique=True)
    brand = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=4, null=True)
    color = models.CharField(max_length=255, null=True)
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="-")
    status = models.IntegerField(choices=CAR_STATUS, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.brand} {self.model} {self.year}"


class Reservation(models.Model):
    reservation_code = models.CharField(max_length=6, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    pickup_date = models.DateTimeField()
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=RESERVATION_STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car.car_code


class ReservationReceipt(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    receipt_no = models.CharField(max_length=12, unique=True)
    description = models.TextField(default="-")
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.IntegerField(choices=PAYMENT_METHOD)
    remark = models.CharField(max_length=255, default="-", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Finance(models.Model):
    finance_code = models.CharField(max_length=12, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    status = models.IntegerField(choices=FINANCE_STATUS, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Period(models.Model):
    period = models.IntegerField()
    finance = models.ForeignKey(Finance, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    pay_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.finance.finance_code} {self.period}"


class PeriodReceipt(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    receipt_no = models.CharField(max_length=12, unique=True)
    issue_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.IntegerField(choices=PAYMENT_METHOD)
    remark = models.TextField(default="-")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.IntegerField(choices=PAYMENT_METHOD)
    sale_status = models.IntegerField(choices=(

    ))
    finance = models.ForeignKey(Finance, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SaleReceipt(models.Model):
    receipt_id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    issue_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.IntegerField(choices=PAYMENT_METHOD)
    remark = models.CharField(max_length=255, default="-", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
