from django import forms

# from dal import autocomplete

from .models import Book, Cost


class BookForm(forms.ModelForm):

    
    class Meta:
        model = Book
        # fields = ('__all__')
        fields = ['name', 'pages', 'author', 'publisher',]

class CostForm(forms.ModelForm):

    
    class Meta:
        model = Cost
        # fields = ('__all__')
        fields = ['book', 'cost',]