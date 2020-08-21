from django.urls import path, include
from .views import AuthorListView, AuthorCreateView, \
     AuthorUpdateView, AuthorDeleteView, \
         AuthorDetailView, 
         

from .models import Author


app_name = 'author'

urlpatterns = [
    path('all/', AuthorListView.as_view(), name='author_list'),
    path('detail/<slug:slug>/', AuthorDetailView.as_view(), name = 'author_detail'),
    path('create/', AuthorCreateView.as_view(), name = 'author_create'),
    path('update/<slug:slug>/', AuthorUpdateView.as_view(), name = 'author_update'),
    path('delete/<slug:slug>/', AuthorDeleteView.as_view(), name = 'author_delete'),
]