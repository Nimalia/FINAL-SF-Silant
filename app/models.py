from django.db import models
from datetime import datetime
from rest_framework.reverse import reverse
from roles.models import CustomUser


# Техника.Справочники:
class VehicleModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Модель техники')

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'

    def __str__(self):
        return self.name
    
class EngineModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Модель двигателя')

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателя'

    def __str__(self):
        return self.name    

class TransmissionModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Модель трансмиссии')

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссии'

    def __str__(self):
        return self.name

class LeadAxleModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Модель ведущего моста')

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущего моста'

    def __str__(self):
        return self.name

class SteerAxleModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Модель управляемого моста')

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемого моста'

    def __str__(self):
        return self.name

class Client(models.Model):

    name = models.ForeignKey(CustomUser, verbose_name='Клиент', on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name}'

class ServiceCompany(models.Model):
    name = models.ForeignKey(CustomUser, verbose_name='Сервисная компания', on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Cервисные компании'

    def __str__(self):
        return f'{self.name}'
    
# таблица Техника:
class Vehicle(models.Model):
    serial_number = models.CharField(max_length=50, unique=True, verbose_name='Зав. № машины')
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, verbose_name='Модель техники', related_name='vehicle_model')
    engine_model = models.ForeignKey(EngineModel, on_delete=models.CASCADE, verbose_name='Модель двигателя', related_name='engine_model')
    engine_serial_number = models.CharField(max_length=50, verbose_name='Зав. № двигателя')
    transmission_model = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE, verbose_name='Модель трансмиссии', related_name='transmission_model')
    transmission_serial_number = models.CharField(max_length=50, verbose_name='Зав. № трансмиссии')
    leading_axle_model = models.ForeignKey(LeadAxleModel, on_delete=models.CASCADE, verbose_name='Модель ведущего моста', related_name='leading_axle_model')
    leading_axle_serial_number = models.CharField(max_length=50, verbose_name='Зав. № ведущего моста')
    steering_axle_model = models.ForeignKey(SteerAxleModel, on_delete=models.CASCADE, verbose_name='Модель управляемого моста', related_name='steering_axle_model')
    steering_axle_serial_number = models.CharField(max_length=50, verbose_name='Зав. № управляемого моста')
    contract = models.CharField(max_length=50, verbose_name='Договор поставки №, дата')
    delivery_date = models.DateField(verbose_name='Дата отгрузки с завода')
    consignee = models.CharField(max_length=50, verbose_name='Грузополучатель (конечный потребитель)')
    delivery_address = models.CharField(max_length=50, verbose_name='Адрес поставки (эксплуатации)')
    fullset = models.TextField(verbose_name='Комплектация (доп. опции)', default="Стандарт")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', related_name='client')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания', related_name='service_company')

    def __str__(self):
        return f'{self.serial_number}'

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'



# Тех обслуживание. Справочники:
class TechserviceType(models.Model):
    name = models.CharField(max_length=50, verbose_name='Вид тех.обслуживания')

    class Meta:
        verbose_name = 'Вид тех.обслуживания'
        verbose_name_plural = 'Виды тех.обслуживания'

    def __str__(self):
        return self.name

# таблица Тех обслуживание:
class Techservice(models.Model):
    techservicetype = models.ForeignKey(TechserviceType, on_delete=models.CASCADE, verbose_name='Вид тех.обслуживания', related_name='techservicetype')
    date = models.DateField(default=datetime.now, verbose_name='Дата проведения тех.обслуживания')
    operating_time = models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')
    order_number = models.CharField(max_length=20, verbose_name='№ заказ-наряда')
    order_date = models.DateField(default=datetime.now, verbose_name='Дата заказ-наряда')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Организация, проводившая тех.обслуживание', null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Техника')

    def __str__(self):
        return f'{self.date} {self.vehicle}'

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'


# Рекламация. Справочники:
class FailureNode(models.Model):
    name = models.CharField(max_length=50, verbose_name='Узел отказа')

    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узлы отказа'

    def __str__(self):
        return self.name

class RecoveryMethod(models.Model):
    name = models.CharField(max_length=50, verbose_name='Способ восстановления')

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'

    def __str__(self):
        return self.name
    
class DescriptionFailure(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Описание отказа'
        verbose_name_plural = 'Описания отказа'


# таблица Рекламация:
class Claim(models.Model):
    failure_date = models.DateField(verbose_name='Дата отказа', default=datetime.now)
    operating_time = models.FloatField(verbose_name='Наработка, м/час')
    failure_node = models.ForeignKey(FailureNode, on_delete=models.CASCADE, verbose_name='Узел отказа', related_name='failure_node')
    description_failure = models.ForeignKey(DescriptionFailure, verbose_name='Описание отказа', on_delete=models.CASCADE, related_name='description_failure')
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE, verbose_name='Способ восстановления', related_name='recovery_method')
    used_spare_parts = models.TextField(verbose_name='Используемые запасные части')
    recovery_date = models.DateField(verbose_name='Дата восстановления', default=datetime.now)
    downtime = models.FloatField(verbose_name='Время простоя техники')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Техника')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.failure_date} {self.vehicle}'
 
    def downtime(self):
        deltatime = self.recovery_date - self.failure_date        
        return deltatime.days

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
    