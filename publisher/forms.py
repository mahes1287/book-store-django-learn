from django import forms

# from dal import autocomplete

from .models import Publisher


class PublisherForm(forms.ModelForm):

    
    class Meta:
        model = Publisher
        # fields = ('__all__')
        fields = ['name', 'address_line', 'city', 'state', 'country', 'pincode',]