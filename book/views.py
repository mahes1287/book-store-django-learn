from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import Book, Cost, Language, Genre
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .forms import BookForm, CostForm, LanguageForm, GenreForm

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

class CostDeleteView(DeleteView):
    model = Cost
    template_name = 'cost/cost_confirm_delete.html'
    success_url = reverse_lazy('cost:cost_list')

# language related viwes

class LanguageListView(ListView):
    model = Language
    context_object_name = 'language_list'
    template_name = 'language/language_list.html'

class LanguageDetailView(DetailView):
    model = Language
    context_object_name = 'language'
    template_name = 'language/language_detail.html'

class LanguageCreateView(CreateView):
    model = Language
    template_name = 'language/language_form.html'
    form_class = LanguageForm

class LanguageUpdateView(UpdateView):
    model = Language
    template_name = 'language/language_form.html'
    form_class = LanguageForm

class LanguageStatusUpdateView(UpdateView):
    model = Language
    template_name = 'language/language_form.html'
    form_class = LanguageForm

class LanguageDeleteView(DeleteView):
    model = Language
    template_name = 'language/language_confirm_delete.html'
    success_url = reverse_lazy('book:language_list')


# genre related viwes

class GenreListView(ListView):
    model = Genre
    context_object_name = 'genre_list'
    template_name = 'genre/genre_list.html'

class GenreDetailView(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'genre/genre_detail.html'

class GenreCreateView(CreateView):
    model = Genre
    template_name = 'genre/genre_form.html'
    form_class = GenreForm

class GenreUpdateView(UpdateView):
    model = Genre
    template_name = 'genre/genre_form.html'
    form_class = GenreForm

class GenreStatusUpdateView(UpdateView):
    model = Genre
    template_name = 'genre/genre_form.html'
    form_class = GenreForm

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'genre/genre_confirm_delete.html'
    success_url = reverse_lazy('book:genre_list')