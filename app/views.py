from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.permissions import IsAuthenticated
from .models import *
from .forms import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from django.db.models import F


# Шаблон
class IndexView(TemplateView):
    template_name = '/index.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('vehicle_list')
        else:
            return redirect('vehicle_search')

# Техника
class VehicleCreateView(LoginRequiredMixin, CreateView):
    permission_required = 'app.create_vehicle'
    model = Vehicle
    form_class = VehicleForm
    template_name = 'app/vehicle_create.html'
    success_url = reverse_lazy('vehicle_list')


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    permission_required = 'app.delete_vehicle'
    model = Vehicle
    template_name_suffix = '_delete'
    success_url = reverse_lazy('vehicle_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicle_model"] = 'vehicle'
        return context
    

class VehicleDetailView(LoginRequiredMixin, DetailView):
    permission_required = 'app.detail_vehicle'
    model = Vehicle
    template_name = 'app/vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VehicleSearchView(ListView):
    model = Vehicle
    template_name = 'app/vehicle_search.html'
    context_object_name = 'vehicles' 

    def get_queryset(self):
        vehicles = Vehicle.objects.all()
        return vehicles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicles = self.get_queryset()
        page = self.request.GET.get('page', 1)
        paginator = Paginator(vehicles, 10)

        try:
            vehicles = paginator.page(page)
        except PageNotAnInteger:
            vehicles = paginator.page(1)
        except EmptyPage:
            vehicles = paginator.page(paginator.num_pages)

        context['vehicles'] = vehicles 
        return context


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    permission_required = 'app.update_vehicle'
    model = Vehicle
    form_class = VehicleForm
    template_name = 'app/vehicle_update.html'
    success_url = reverse_lazy('vehicle_list')


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'app/vehicle_list.html'

    def get(self, request, *args, **kwargs):
        order_by = request.GET.get('ordering', 'delivery_date')

        if not request.user.is_staff:
            user = CustomUser.objects.get(pk=request.user.pk)
            try:
                clients = Client.objects.get(name_id=user)
                vehicles = Vehicle.objects.filter(client=clients)
            except:
                service_company = ServiceCompany.objects.get(name_id=user)
                vehicles = Vehicle.objects.filter(service_company=service_company)
        else:
            vehicles = Vehicle.objects.all()

        # Пагинация
        paginator = Paginator(vehicles.order_by(order_by), 10)  # 10 - количество объектов на странице
        page = request.GET.get('page')

        try:
            vehicles = paginator.page(page)
        except PageNotAnInteger:
            vehicles = paginator.page(1)
        except EmptyPage:
            vehicles = paginator.page(paginator.num_pages)

        context = {
            'object_list': vehicles,
            'ordering': order_by,
        }

        return render(request, self.template_name, context)



class VehicleDetailsView(TemplateView):
    template_name = 'app/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = Vehicle.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'vehicle_model':
            context['atribute'] = vehicle.vehicle_model

        elif atribute == 'engine_model':
            context['atribute'] = vehicle.engine_model

        elif atribute == 'transmission_model':
            context['atribute'] = vehicle.transmission_model
            
        elif atribute == 'leading_axle_model':
            context['atribute'] = vehicle.leading_axle_model
            
        elif atribute == 'steering_axle_model':
            context['atribute'] = vehicle.steering_axle_model
            
        elif atribute == 'fullset':
            context['atribute'] = vehicle.fullset
            
        elif atribute == 'service_company':
            context['atribute'] = vehicle.service_company

        return context


# Тех обслуживание
class TechserviceCreateView(LoginRequiredMixin, CreateView):
    permission_required = 'techservice.create_techservice'
    model = Techservice
    form_class = TechserviceForm
    template_name = 'app/techservice_create.html'
    success_url = reverse_lazy('techservice_list')


class TechserviceDeleteView(LoginRequiredMixin, DeleteView):
    permission_required = 'app.delete_techservice'
    model = Techservice
    template_name_suffix = '_delete'
    success_url = reverse_lazy('techservice_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["techservicetype"] = 'techservice'
        return context
    

class TechserviceDetailView(LoginRequiredMixin, ListView):
    permission_required = 'app.detail_techservice'
    model = Techservice
    template_name = 'app/techservice_detail.html'

    def get_queryset(self):
        vehicle = Vehicle.objects.get(pk=self.kwargs["pk"])
        return Techservice.objects.filter(vehicle=vehicle)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicle"] = Vehicle.objects.get(pk=self.kwargs["pk"])
        return context
    

class TechserviceUpdateView(LoginRequiredMixin, UpdateView):
    permission_required = 'app.update_techservice'
    model = Techservice
    form_class = TechserviceForm
    template_name = 'app/techservice_update.html'
    success_url = reverse_lazy('techservice_list')
    

class TechserviceListView(LoginRequiredMixin, ListView):
    permission_required = 'app.techservice'
    model = Techservice
    template_name = 'app/techservice_list.html'
    context_object_name = 'techservice'
    ordering = 'date'

    def get_queryset(self):
        user = self.request.user
        ordering = self.request.GET.get('ordering', 'date')

        if user.is_staff:
            queryset = Techservice.objects.all()
        else:
            try:
                client = Client.objects.get(name=user)
                vehicles = Vehicle.objects.filter(client=client)
                queryset = Techservice.objects.filter(vehicle__in=vehicles)
            except Client.DoesNotExist:
                try:
                    service_company = ServiceCompany.objects.get(name=user)
                    vehicles = Vehicle.objects.filter(service_company=service_company)
                    queryset = Techservice.objects.filter(vehicle__in=vehicles)
                except ServiceCompany.DoesNotExist:
                    queryset = Techservice.objects.none()

        # Обработка сортировки по заголовкам таблицы
        if ordering == 'date':
            queryset = queryset.order_by(F('date').asc(nulls_last=True))
        elif ordering == 'techservicetype':
            queryset = queryset.order_by(F('techservicetype').asc(nulls_last=True))
        elif ordering == 'operating_time':
            queryset = queryset.order_by(F('operating_time').asc(nulls_last=True))
        elif ordering == 'order_number':
            queryset = queryset.order_by(F('order_number').asc(nulls_last=True))
        elif ordering == 'order_date':
            queryset = queryset.order_by(F('order_date').asc(nulls_last=True))
        elif ordering == 'vehicle':
            queryset = queryset.order_by(F('vehicle').asc(nulls_last=True))
        elif ordering == 'service_company':
            queryset = queryset.order_by(F('service_company').asc(nulls_last=True))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        techservices = self.get_queryset()
        page = self.request.GET.get('page', 1)
        paginator = Paginator(techservices, 10)

        try:
            techservices = paginator.page(page)
        except PageNotAnInteger:
            techservices = paginator.page(1)
        except EmptyPage:
            techservices = paginator.page(paginator.num_pages)

        context['techservice'] = techservices
        return context
        


class TechserviceDetailsView(TemplateView):
    template_name = 'app/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        techservice = Techservice.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'type':
            context['atribute'] = techservice.techservicetype
            
        elif atribute == 'service_company':
            context['atribute'] = techservice.service_company
            
        return context


# Рекламация
class ClaimCreateView(LoginRequiredMixin, CreateView):
    permission_required = 'app.create_claim'
    model = Claim
    form_class = ClaimForm
    template_name = 'app/claim_create.html'
    success_url = reverse_lazy('claim_list')


class ClaimDeleteView(LoginRequiredMixin, DeleteView):
    permission_required = 'app.delete_claim'
    model = Claim
    template_name_suffix = '_delete'
    success_url = reverse_lazy('claim_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'claim'
        return context


class ClaimDetailView(LoginRequiredMixin, ListView):
    permission_required = 'app.detail_claim'
    model = Claim
    template_name = 'app/claim_detail.html'

    def get_queryset(self):
        vehicle = Vehicle.objects.get(pk=self.kwargs["pk"])
        return Claim.objects.filter(vehicle=vehicle)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicle"] = Vehicle.objects.get(pk=self.kwargs["pk"])
        return context


class ClaimUpdateView(LoginRequiredMixin, UpdateView):
    permission_required = 'app.update_claim'
    model = Claim
    form_class = ClaimForm
    template_name = 'app/claim_update.html'
    success_url = reverse_lazy('claim_list')


class ClaimListView(LoginRequiredMixin, ListView):
    permission_required = 'app.view_claim'
    model = Claim
    template_name = 'app/claim_list.html'
    ordering = 'failure_date'
    context_object_name = 'claim_list'
    paginate_by = 10  # количество на каждой странице

    def get_queryset(self):
        user = self.request.user
        ordering = self.request.GET.get('ordering', 'failure_date')  

        if user.is_staff:
            return Claim.objects.all().order_by(ordering)
        else:
            try:
                client = Client.objects.get(name=user)
                vehicles = Vehicle.objects.filter(client=client)
                return Claim.objects.filter(vehicle__in=vehicles).order_by(ordering)
            except Client.DoesNotExist:
                try:
                    service_company = ServiceCompany.objects.get(name=user)
                    vehicles = Vehicle.objects.filter(service_company=service_company)
                    return Claim.objects.filter(vehicle__in=vehicles).order_by(ordering)
                except ServiceCompany.DoesNotExist:
                    return Claim.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        claims = self.get_queryset()
        page = self.request.GET.get('page', 1)
        paginator = Paginator(claims, self.paginate_by)

        try:
            claims = paginator.page(page)
        except PageNotAnInteger:
            claims = paginator.page(1)
        except EmptyPage:
            claims = paginator.page(paginator.num_pages)

        context['claim_list'] = claims
        return context
                

class ClaimDetailsView(TemplateView):
    template_name = 'app/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        claim = Claim.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'failure_node':
            context['atribute'] = claim.failure_node
            
        elif atribute == 'recovery_method':
            context['atribute'] = claim.recovery_method
            
        elif atribute == 'vehicle':
            context['atribute'] = claim.vehicle
            
        elif atribute == 'service_company':
            context['atribute'] = claim.service_company

        return context
    

# API Техника
class VehicleDetailAPI(generics.RetrieveAPIView):
    serializer_class = VehicleSerializer

    def get_object(self):
        obj = Vehicle.objects.get(pk=self.kwargs['pk'])
        return obj

class VehiclerListAPI(generics.ListAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class VehicleUserListAPI(generics.ListAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Vehicle.objects.filter(client=user)
        elif type(user) == str:
            queryset = Vehicle.objects.filter(client__username=user)
        return queryset


# API Тех обслуживание
class TechserviceDetailAPI(generics.RetrieveAPIView):
    serializer_class = TechserviceSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = Techservice.objects.get(pk=self.kwargs['pk'])
        return obj


class TechserviceListAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TechserviceSerializer
    queryset = Techservice.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class TechserviceUserListAPI(generics.ListAPIView):
    serializer_class = TechserviceSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj



# API Рекламация
class ClaimDetailAPI(generics.RetrieveAPIView):
    serializer_class = ClaimSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    

class ClaimListAPI(generics.ListAPIView):
    serializer_class = ClaimSerializer
    queryset = Claim.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class ClaimUserListAPI(generics.ListAPIView):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Claim.objects.filter(car__client=user)
        elif type(user) == str:
            queryset = Claim.objects.filter(car__client__username=user)
        return queryset


# viewsets Техника 
class VehicleModelViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer


class EngineModelViewSet(viewsets.ModelViewSet):
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer


class TransmissionModelViewSet(viewsets.ModelViewSet):
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer


class LeadAxleModelViewSet(viewsets.ModelViewSet):
    queryset = LeadAxleModel.objects.all()
    serializer_class = LeadAxleModelSerializer


class SteerAxleModelViewSet(viewsets.ModelViewSet):
    queryset = SteerAxleModel.objects.all()
    serializer_class = SteerAxleModelSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ServiceCompanyViewSet(viewsets.ModelViewSet):
    queryset = ServiceCompany.objects.all()
    serializer_class = ServiceCompanySerializer
    permission_classes = []


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


# viewsets Тех обслуживание
class TechserviceTypeViewSet(viewsets.ModelViewSet):
    queryset = TechserviceType.objects.all()
    serializer_class = TechserviceTypeSerializer


class TechserviceViewSet(viewsets.ModelViewSet):
    queryset = Techservice.objects.all()
    serializer_class = TechserviceSerializer


# viewsets Рекламация
class FailureNodeViewSet(viewsets.ModelViewSet):
    queryset = FailureNode.objects.all()
    serializer_class = FailureNodeSerializer


class DescriptionFailureViewSet(viewsets.ModelViewSet):
    queryset = DescriptionFailure.objects.all()
    serializer_class = DescriptionFailureSerializer


class RecoveryMethodViewSet(viewsets.ModelViewSet):
    queryset = RecoveryMethod.objects.all()
    serializer_class = RecoveryMethodSerializer


class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer











