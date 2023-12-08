from rest_framework import routers
from app.views import *


router = routers.DefaultRouter()

router.register('vehicle_model', VehicleModelViewSet)
router.register('engine_model', EngineModelViewSet)
router.register('transmission_model', TransmissionModelViewSet)
router.register('leading_axle_model', LeadAxleModelViewSet)
router.register('steering_axle_model', SteerAxleModelViewSet)
router.register('client', ClientViewSet)
router.register('service_company', ServiceCompanyViewSet)
router.register('vehicle', VehicleViewSet)

router.register('techservicetype', TechserviceTypeViewSet)
router.register('techservice', TechserviceViewSet)

router.register('failure_node', FailureNodeViewSet)
router.register('description_failure', DescriptionFailureViewSet)
router.register('recovery_method', RecoveryMethodViewSet)
router.register('claim', ClaimViewSet)

