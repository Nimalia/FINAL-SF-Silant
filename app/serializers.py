from rest_framework import serializers
from .models import *


# Техника
class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class EngineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineModel
        fields = '__all__'


class TransmissionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionModel
        fields = '__all__'


class LeadAxleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadAxleModel
        fields = '__all__'


class SteerAxleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteerAxleModel
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


# Тех обслуживание
class TechserviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechserviceType
        fields = '__all__'


class TechserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techservice
        fields = '__all__'


# Рекламация
class FailureNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureNode
        fields = '__all__'


class DescriptionFailureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionFailure
        fields = '__all__'


class RecoveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryMethod
        fields = '__all__'


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'