from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from .models import *


# Модель машины
class VehicleModelResource(resources.ModelResource):
    class Meta:
        model = VehicleModel
        report_skipped = True
        fields = ('id', 'name')

@admin.register(VehicleModel)
class VehicleModelAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = VehicleModelResource
    list_display = ('id', 'name')
    filter = ('name')


# Модель двигателя
class EngineModelResource(resources.ModelResource):
    class Meta:
        model = EngineModel
        report_skipped = True
        fields = ('id', 'name',)


@admin.register(EngineModel)
class EngineModelAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = EngineModelResource
    list_display = ('id', 'name',)
    filter = ('name',)


# Модель трансмиссии
class TransmissionModelResource(resources.ModelResource):
    class Meta:
        model = TransmissionModel
        report_skipped = True
        fields = ('id', 'name')


@admin.register(TransmissionModel)
class TransmissionModelAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TransmissionModelResource
    list_display = ('id', 'name')
    filter = ('name')


# Модель ведущего моста
class LeadAxleModelResource(resources.ModelResource):
    class Meta:
        model = LeadAxleModel
        report_skipped = True
        fields = ('id', 'name')


@admin.register(LeadAxleModel)
class LeadAxleModelAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = LeadAxleModelResource
    list_display = ('id', 'name')
    filter = ('name',)


# Модель управляемого мост
class SteerAxleModelResource(resources.ModelResource):
    class Meta:
        model = SteerAxleModel
        report_skipped = True
        fields = ('id', 'name')


@admin.register(SteerAxleModel)
class SteerAxleModelAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SteerAxleModelResource
    list_display = ('id', 'name')
    filter = ('name')


# Клиент
class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        report_skipped = True
        fields = ('id', 'name')


@admin.register(Client)
class ClientAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ClientResource
    list_display = ('id', 'name')
    filter = ('name')


# Сервисная организация
class ServiceCompanyResource(resources.ModelResource):
    class Meta:
        model = ServiceCompany
        report_skipped = True
        fields = ('id', 'name')


@admin.register(ServiceCompany)
class SersviceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ServiceCompanyResource
    list_display = ('id', 'name')
    filter = ('name')


# Техника 
class VehicleResource(resources.ModelResource):
    class Meta:
        model = Vehicle
        report_skipped = True
        fields = ('serial_number',
                  'vehicle_model',
                  'engine_model',
                  'engine_serial_number',
                  'transmission_model',
                  'transmission_serial_number',
                  'leading_axle_model',
                  'leading_axle_serial_number',
                  'steering_axle_model',
                  'steering_axle_serial_number',
                  'contract',
                  'delivery_date',
                  'consignee',
                  'delivery_address',
                  'fullset',
                  'client',
                  'service_company',
                  )


@admin.register(Vehicle)
class VehicleAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = VehicleResource
    list_display = ('serial_number',
                    'vehicle_model',
                    'engine_model',
                    'transmission_model',
                    'leading_axle_model',
                    'steering_axle_model',
                    'delivery_date',
                    'fullset',
                    'client',
                    'service_company',
                    )
    filter = ('serial_number',)


# Вид Тех обслуживания
class TechserviceTypeResource(resources.ModelResource):
    class Meta:
        model = TechserviceType
        report_skipped = True
        fields = ('id', 'name')


@admin.register(TechserviceType)
class TechserviceTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TechserviceTypeResource
    list_display = ('id', 'name')
    filter = ('name')

# Тех обслуживание:
class TechserviceResource(resources.ModelResource):
    class Meta:
        model = Techservice
        report_skipped = True
        fields = ('techservicetype',
                  'date',
                  'operating_time',
                  'order_number',
                  'order_date',
                  'service_company',
                  'vehicle',
                  )


@admin.register(Techservice)
class TechserviceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TechserviceResource
    list_display = ('vehicle',
                    'techservicetype',
                    'date',
                    'operating_time',
                    'order_number',
                    'order_date',
                    'service_company',
                    )
    filter = ('vehicle',)


# Узел отказа
class FailureNodeResource(resources.ModelResource):
    class Meta:
        model = FailureNode
        report_skipped = True
        fields = ('id', 'name')


@admin.register(FailureNode)
class FailureNodeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FailureNodeResource
    list_display = ('id', 'name')
    filter = ('name')


# Способ восстановления
class RecoveryMethodResource(resources.ModelResource):
    class Meta:
        model = RecoveryMethod
        report_skipped = True
        fields = ('id', 'name')


@admin.register(RecoveryMethod)
class RecoveryMethodAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = RecoveryMethodResource
    list_display = ('id', 'name')
    filter = ('name')


# Описание отказа
class DescriptionFailureResource(resources.ModelResource):
    class Meta:
        model = DescriptionFailure
        report_skipped = True
        fields = ('id', 'name')


@admin.register(DescriptionFailure)
class DescriptionFailureAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DescriptionFailureResource
    list_display = ('id', 'name')
    filter = ('name')


# Рекламация
class ClaimResource(resources.ModelResource):
    class Meta:
        model = Claim
        report_skipped = True
        fields = ('vehicle',
                  'failure_date',
                  'operating_time',
                  'failure_node',
                  'description_failure',
                  'recovery_method',
                  'used_spare_parts',
                  'recovery_date',
                  'downtime',
                  )


@admin.register(Claim)
class ClaimAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ClaimResource
    list_display = ('vehicle',
                    'failure_date',
                    'operating_time',
                    'failure_node',
                    'description_failure',
                    'recovery_method',
                    'used_spare_parts',
                    'recovery_date',
                    'downtime',
                    )
    filter = ('vehicle')


