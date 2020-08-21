from django.urls import path, include
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView 
from .views import CostListView, CostCreateView, CostUpdateView, CostDeleteView, CostDetailView
from .models import Book, Cost

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


]