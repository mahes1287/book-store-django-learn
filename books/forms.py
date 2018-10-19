# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Book
from django.forms.widgets import SelectDateWidget


class BookForm(ModelForm):
    """
    Build form from Book model. Allow editing of book information.
    """
    class Meta:
        model = Book
        fields = ['book_title', 'authors_info', 'isbn', 'price', 'date_publish']
        labels = {
            'book_title': _('Book title'),
            'authors_info': _('Book authors'),
            'isbn': _('International standard book number'),
            'price': _('Book price'),
            'date_publish': _('Book publish date'),
        }
        widgets = {
            'date_publish': SelectDateWidget(empty_label="Choose date", years=range(1950, 2051))
        }