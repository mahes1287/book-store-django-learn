from django.urls import path, include
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView 
from .views import CostListView, CostCreateView, CostUpdateView, CostDeleteView, CostDetailView
from .views import LanguageListView, LanguageCreateView, LanguageUpdateView, LanguageDeleteView, LanguageDetailView
from .views import GenreListView, GenreCreateView, GenreUpdateView, GenreDeleteView, GenreDetailView
from .models import Book, Cost, Language, Genre

app_name = 'book'

urlpatterns = [

    path('all/', BookListView.as_view(), name='book_list'),
    path('detail/<slug:slug>/', BookDetailView.as_view(), name = 'book_detail'),
    path('create/', BookCreateView.as_view(), name = 'book_create'),
    path('update/<slug:slug>/', BookUpdateView.as_view(), name = 'book_update'),
    path('delete/<slug:slug>/', BookDeleteView.as_view(), name = 'book_delete'),

# Cost urls
    path('cost/all/', CostListView.as_view(), name='cost_list'),
    path('cost/detail/<slug:slug>/', CostDetailView.as_view(), name = 'cost_detail'),
    path('cost/create/', CostCreateView.as_view(), name = 'cost_create'),
    path('cost/update/<slug:slug>/', CostUpdateView.as_view(), name = 'cost_update'),
    path('cost/delete/<slug:slug>/', CostDeleteView.as_view(), name = 'cost_delete'),

# Genre urls
    path('genre/all/', GenreListView.as_view(), name='genre_list'),
    path('genre/detail/<slug:slug>/', GenreDetailView.as_view(), name = 'genre_detail'),
    path('genre/create/', GenreCreateView.as_view(), name = 'genre_create'),
    path('genre/update/<slug:slug>/', GenreUpdateView.as_view(), name = 'genre_update'),
    path('genre/delete/<slug:slug>/', GenreDeleteView.as_view(), name = 'genre_delete'),

# Language urls
    path('language/all/', LanguageListView.as_view(), name='language_list'),
    path('language/detail/<slug:slug>/', LanguageDetailView.as_view(), name = 'language_detail'),
    path('language/create/', LanguageCreateView.as_view(), name = 'language_create'),
    path('language/update/<slug:slug>/', LanguageUpdateView.as_view(), name = 'language_update'),
    path('language/delete/<slug:slug>/', LanguageDeleteView.as_view(), name = 'language_delete'),
]