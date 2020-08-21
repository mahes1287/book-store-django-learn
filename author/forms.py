from django import forms

# from dal import autocomplete

from .models import Author


class AuthorForm(forms.ModelForm):

    
    class Meta:
        model = Author
        # fields = ('__all__')
        fields = ['name', 'country', ]