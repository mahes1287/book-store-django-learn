from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import Author
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .forms import AuthorForm


class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'author/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'author/author_detail.html'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author/author_form.html'
    form_class = AuthorForm

class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author/author_form.html'
    form_class = AuthorForm

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/author_confirm_delete.html'
    success_url = reverse_lazy('author:author_list')
