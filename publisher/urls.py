from django.urls import path, include
from .views import PublisherListView, PublisherCreateView, PublisherUpdateView, PublisherDeleteView, PublisherDetailView
from .views import CountryListView, CountryCreateView, CountryUpdateView, CountryDeleteView, CountryDetailView
from .views import StateListView, StateCreateView, StateUpdateView, StateDeleteView, StateDetailView
from .views import DistrictListView, DistrictCreateView, DistrictUpdateView, DistrictDeleteView, DistrictDetailView
from .models import Publisher, Country, State, District

app_name = 'publisher'

urlpatterns = [
    path('all/', PublisherListView.as_view(), name='publisher_list'),
    path('detail/<slug:slug>/', PublisherDetailView.as_view(), name = 'publisher_detail'),
    path('create/', PublisherCreateView.as_view(), name = 'publisher_create'),
    path('update/<slug:slug>/', PublisherUpdateView.as_view(), name = 'publisher_update'),
    path('delete/<slug:slug>/', PublisherDeleteView.as_view(), name = 'publisher_delete'),

#Country URLs
    path('country/all/', CountryListView.as_view(), name='country_list'),
    path('country/detail/<slug:slug>/', CountryDetailView.as_view(), name = 'country_detail'),
    path('country/create/', CountryCreateView.as_view(), name = 'country_create'),
    path('country/update/<slug:slug>/', CountryUpdateView.as_view(), name = 'country_update'),
    path('country/delete/<slug:slug>/', CountryDeleteView.as_view(), name = 'country_delete'),

#State URLs
    path('state/all/', StateListView.as_view(), name='state_list'),
    path('state/detail/<slug:slug>/', StateDetailView.as_view(), name = 'state_detail'),
    path('state/create/', StateCreateView.as_view(), name = 'state_create'),
    path('state/update/<slug:slug>/', StateUpdateView.as_view(), name = 'state_update'),
    path('state/delete/<slug:slug>/', StateDeleteView.as_view(), name = 'state_delete'),

#District URLs
    path('district/all/', DistrictListView.as_view(), name='district_list'),
    path('district/detail/<slug:slug>/', DistrictDetailView.as_view(), name = 'district_detail'),
    path('district/create/', DistrictCreateView.as_view(), name = 'district_create'),
    path('district/update/<slug:slug>/', DistrictUpdateView.as_view(), name = 'district_update'),
    path('district/delete/<slug:slug>/', DistrictDeleteView.as_view(), name = 'district_delete'),
]