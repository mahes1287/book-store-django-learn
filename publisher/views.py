from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import Publisher, Country, State, District
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .forms import PublisherForm, CountryForm, StateForm, DistrictForm


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publisher_list'
    template_name = 'publisher/publisher_list.html'

class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = 'publisher'
    template_name = 'publisher/publisher_detail.html'

class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'publisher/publisher_form.html'
    form_class = PublisherForm

class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'publisher/publisher_form.html'
    form_class = PublisherForm

class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publisher/publisher_confirm_delete.html'
    success_url = reverse_lazy('publisher:publisher_list')

# Country views

class CountryListView(ListView):
    model = Country
    context_object_name = 'country_list'
    template_name = 'country/country_list.html'

class CountryDetailView(DetailView):
    model = Country
    context_object_name = 'country'
    template_name = 'country/country_detail.html'

class CountryCreateView(CreateView):
    model = Country
    template_name = 'country/country_form.html'
    form_class = CountryForm

class CountryUpdateView(UpdateView):
    model = Country
    template_name = 'country/country_form.html'
    form_class = CountryForm

class CountryDeleteView(DeleteView):
    model = Country
    template_name = 'country/country_confirm_delete.html'
    success_url = reverse_lazy('publisher:country_list')

# State views

class StateListView(ListView):
    model = State
    context_object_name = 'state_list'
    template_name = 'state/state_list.html'

class StateDetailView(DetailView):
    model = State
    context_object_name = 'state'
    template_name = 'state/state_detail.html'

class StateCreateView(CreateView):
    model = State
    template_name = 'state/state_form.html'
    form_class = StateForm

class StateUpdateView(UpdateView):
    model = State
    template_name = 'state/state_form.html'
    form_class = StateForm

class StateDeleteView(DeleteView):
    model = State
    template_name = 'state/state_confirm_delete.html'
    success_url = reverse_lazy('publisher:state_list')


# District views

class DistrictListView(ListView):
    model = District
    context_object_name = 'district_list'
    template_name = 'district/district_list.html'

class DistrictDetailView(DetailView):
    model = District
    context_object_name = 'district'
    template_name = 'district/district_detail.html'

class DistrictCreateView(CreateView):
    model = District
    template_name = 'district/district_form.html'
    form_class = DistrictForm

class DistrictUpdateView(UpdateView):
    model = District
    template_name = 'district/district_form.html'
    form_class = DistrictForm

class DistrictDeleteView(DeleteView):
    model = District
    template_name = 'district/district_confirm_delete.html'
    success_url = reverse_lazy('publisher:district_list')