# Generated by Django 5.0.2 on 2024-02-14 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_code', models.CharField(max_length=8, unique=True)),
                ('brand', models.CharField(max_length=255, null=True)),
                ('model', models.CharField(max_length=255, null=True)),
                ('year', models.CharField(max_length=4, null=True)),
                ('color', models.CharField(max_length=255, null=True)),
                ('mileage', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(default='-')),
                ('status', models.IntegerField(choices=[(1, 'Ready'), (2, 'Reserved'), (3, 'Sold')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_code', models.CharField(max_length=6, unique=True)),
                ('position_name', models.CharField(max_length=255)),
                ('description', models.TextField(default='-')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(max_length=8, unique=True)),
                ('tel', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=255, null=True, unique=True)),
                ('credit_info', models.TextField(null=True)),
                ('address', models.TextField(default=True)),
                ('sub_district', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finance_code', models.CharField(max_length=12, unique=True)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monthly_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Rejected')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField()),
                ('due_date', models.DateTimeField()),
                ('pay_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remark', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('finance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.finance')),
            ],
        ),
        migrations.CreateModel(
            name='PeriodReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_no', models.CharField(max_length=12, unique=True)),
                ('issue_date', models.DateField()),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.IntegerField(choices=[(1, 'Cash'), (2, 'Bank')])),
                ('remark', models.TextField(default='-')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.period')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_code', models.CharField(max_length=6, unique=True)),
                ('tel', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=255, null=True, unique=True)),
                ('address', models.TextField()),
                ('sub_district', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=5)),
                ('start_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.position')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_code', models.CharField(max_length=6, unique=True)),
                ('reservation_date', models.DateTimeField()),
                ('pickup_date', models.DateTimeField()),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.IntegerField(choices=[(1, 'Reserved'), (2, 'Pending'), (3, 'Cancelled')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_no', models.CharField(max_length=12, unique=True)),
                ('description', models.TextField(default='-')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.IntegerField(choices=[(1, 'Cash'), (2, 'Bank')])),
                ('remark', models.CharField(blank=True, default='-', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.IntegerField(choices=[(1, 'Cash'), (2, 'Bank')])),
                ('sale_status', models.IntegerField(choices=[])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.employee')),
                ('finance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tent.finance')),
            ],
        ),
        migrations.CreateModel(
            name='SaleReceipt',
            fields=[
                ('receipt_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.IntegerField(choices=[(1, 'Cash'), (2, 'Bank')])),
                ('remark', models.CharField(blank=True, default='-', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tent.sale')),
            ],
        ),
    ]