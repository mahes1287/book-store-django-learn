from django.urls import path, include
from .views import PublisherListView, PublisherCreateView, \
     PublisherUpdateView, PublisherDeleteView, \
         PublisherDetailView, 
         

from .models import Publisher


app_name = 'publisher'

urlpatterns = [
    path('all/', PublisherListView.as_view(), name='publisher_list'),
    path('detail/<slug:slug>/', PublisherDetailView.as_view(), name = 'publisher_detail'),
    path('create/', PublisherCreateView.as_view(), name = 'publisher_create'),
    path('update/<slug:slug>/', PublisherUpdateView.as_view(), name = 'publisher_update'),
    path('delete/<slug:slug>/', PublisherDeleteView.as_view(), name = 'publisher_delete'),



]