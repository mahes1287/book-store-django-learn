from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import Book, Cost
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .forms import BookForm, #CostForm


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book/book_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book/book_form.html'
    form_class = BookForm

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book/book_form.html'
    form_class = BookForm

class BookStatusUpdateView(UpdateView):
    model = Book
    template_name = 'book/book_form.html'
    form_class = BookForm


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    success_url = reverse_lazy('book:book_list')



 # cost related viwes

 class CostListView(ListView):
    model = Cost
    context_object_name = 'cost_list'
    template_name = 'cost/cost_list.html'

class CostDetailView(DetailView):
    model = Cost
    context_object_name = 'cost'
    template_name = 'cost/cost_detail.html'

class CostCreateView(CreateView):
    model = Cost
    template_name = 'cost/cost_form.html'
    form_class = CostForm

class CostUpdateView(UpdateView):
    model = Cost
    template_name = 'cost/cost_form.html'
    form_class = CostForm

class CostStatusUpdateView(UpdateView):
    model = Cost
    template_name = 'cost/cost_form.html'
    form_class = CostForm


class CostDeleteView(DeleteView):
    model = Cost
    template_name = 'cost/cost_confirm_delete.html'
    success_url = reverse_lazy('cost:cost_list')