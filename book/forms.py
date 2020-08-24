from django import forms

# from dal import autocomplete

from .models import Book, Cost, Genre, Language


class BookForm(forms.ModelForm):

    
	class Meta:
		model = Book
        # fields = ('__all__')
		fields = ['title', 'pages', 'book_type', 'isbn', 'author', 'summary', 'language', 'genre', 'publisher',]


class CostForm(forms.ModelForm):

    
	class Meta:
		model = Cost
        # fields = ('__all__')
		fields = ['book', 'cost',]

class LanguageForm(forms.ModelForm):

    
	class Meta:
		model = Language
        # fields = ('__all__')
		fields = ['name', ]

class GenreForm(forms.ModelForm):

    
	class Meta:
		model = Genre
        # fields = ('__all__')
		fields = ['name', ]