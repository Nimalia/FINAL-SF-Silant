# Generated by Django 4.2.7 on 2023-11-30 08:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failure_date', models.DateField(verbose_name='Дата отказа')),
                ('operating_time', models.FloatField(verbose_name='Наработка, м/час')),
                ('used_spare_parts', models.TextField(verbose_name='Используемые запасные части')),
                ('recovery_date', models.DateField(verbose_name='Дата восстановления')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламации',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='DescriptionFailure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Описание отказа',
                'verbose_name_plural': 'Описания отказов',
            },
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Модель двигателя')),
            ],
        ),
        migrations.CreateModel(
            name='FailureNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Узел отказа')),
            ],
        ),
        migrations.CreateModel(
            name='LeadAxleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Модель ведущего моста')),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Способ восстановления')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сервисная компания',
                'verbose_name_plural': 'Cервисные компании',
            },
        ),
        migrations.CreateModel(
            name='SteerAxleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Модель управляемого моста')),
            ],
        ),
        migrations.CreateModel(
            name='TechserviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Вид тех.обслуживания')),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Модель трансмиссии')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Модель техники')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50, unique=True, verbose_name='Зав. № машины')),
                ('engine_serial_number', models.CharField(max_length=50, verbose_name='Зав. № двигателя')),
                ('transmission_serial_number', models.CharField(max_length=50, verbose_name='Зав. № трансмиссии')),
                ('leading_axle_serial_number', models.CharField(max_length=50, verbose_name='Зав. № ведущего моста')),
                ('steering_axle_serial_number', models.CharField(max_length=50, verbose_name='Зав. № управляемого моста')),
                ('contract', models.CharField(max_length=50, verbose_name='Договор поставки №, дата')),
                ('delivery_date', models.DateField(verbose_name='Дата отгрузки с завода')),
                ('consignee', models.CharField(max_length=50, verbose_name='Грузополучатель (конечный потребитель)')),
                ('delivery_address', models.CharField(max_length=50, verbose_name='Адрес поставки (эксплуатации)')),
                ('fullset', models.TextField(verbose_name='Комплектация (доп. опции)')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='app.client', verbose_name='Клиент')),
                ('engine_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engine_model', to='app.enginemodel', verbose_name='Модель двигателя')),
                ('leading_axle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leading_axle_model', to='app.leadaxlemodel', verbose_name='Модель ведущего моста')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_company', to='app.servicecompany', verbose_name='Сервисная компания')),
                ('steering_axle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steering_axle_model', to='app.steeraxlemodel', verbose_name='Модель управляемого моста')),
                ('transmission_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transmission_model', to='app.transmissionmodel', verbose_name='Модель трансмиссии')),
                ('vehicle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_model', to='app.vehiclemodel', verbose_name='Модель техники')),
            ],
            options={
                'verbose_name': 'Техника',
                'verbose_name_plural': 'Техника',
            },
        ),
        migrations.CreateModel(
            name='Techservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Дата проведения тех.обслуживания')),
                ('operating_time', models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')),
                ('order_number', models.CharField(max_length=20, verbose_name='№ заказ-наряда')),
                ('order_date', models.DateField(default=datetime.datetime.now, verbose_name='Дата заказ-наряда')),
                ('service_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.servicecompany', verbose_name='Организация, проводившая тех.обслуживание')),
                ('techservicetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='techservicetype', to='app.techservicetype', verbose_name='Вид тех.обслуживания')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vehicle', verbose_name='Техника')),
            ],
            options={
                'verbose_name': 'Техническое обслуживание',
                'verbose_name_plural': 'Технические обслуживания',
            },
        ),
    ]
