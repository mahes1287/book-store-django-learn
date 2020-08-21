from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import Publisher
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .forms import PublisherForm


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
