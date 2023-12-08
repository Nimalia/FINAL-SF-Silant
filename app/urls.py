from django.urls import path
from .views import *


urlpatterns = [
    path('techservice/', TechserviceListView.as_view(), name='techservice_list'),
    path('claim/', ClaimListView.as_view(), name='claim_list'),
    path('vehicle/<pk>/techservice', TechserviceDetailView.as_view(), name='techservice_detail'),
    path('vehicle/<pk>/claim', ClaimDetailView.as_view(), name='claim_detail'),
    path('techservice/create', TechserviceCreateView.as_view(), name='techservice_create'),
    path('claim/create', ClaimCreateView.as_view(), name='claim_create'),
    path('techservice/<pk>/update', TechserviceUpdateView.as_view(), name='techservice_update'),
    path('claim/<pk>/update', ClaimUpdateView.as_view(), name='claim_update'),
    path('techservice/<pk>/delete', TechserviceDeleteView.as_view(), name='techservice_delete'),
    path('claim/<pk>/delete', ClaimDeleteView.as_view(), name='claim_delete'),
    path('techservice/<pk>/description/<atribute>', TechserviceDetailsView.as_view(),
         name='techservice_details'),
    path('claim/<pk>/description/<atribute>', ClaimDetailsView.as_view(), name='claim_details'),

    path('', IndexView.as_view(template_name='/index.html'), name='index'),
    path('search/', VehicleSearchView.as_view(), name='vehicle_search'),
    path('vehicles/', VehicleListView.as_view(), name='vehicle_list'),
    path('vehicle/<pk>/detail', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicle/create', VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicle/<pk>/update', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicle/<pk>/delete', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicle/<pk>/description/<atribute>', VehicleDetailsView.as_view(), name='vehicle_details'),
]


