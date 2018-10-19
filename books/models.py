# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.urls import reverse


class Book(models.Model):
    """
    Book model with title, authors, international standard book number(ISBN), price
    and date publish
    """
    book_title = models.CharField(max_length=100)
    authors_info = models.CharField(max_length=150)
    isbn = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_publish = models.DateField(default=date.today)

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        """
        This function return obsolute pass for template.
        """
        return reverse('book-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['date_publish']


class SaveHttpRequests(models.Model):
    request_method = models.CharField(max_length=6)
    request_path = models.CharField(max_length=150)
    request_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-request_datetime']

