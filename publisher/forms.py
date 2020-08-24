from django import forms

# from dal import autocomplete

from .models import Publisher, Country, State, District


class PublisherForm(forms.ModelForm):

    
    class Meta:
        model = Publisher
        # fields = ('__all__')
        fields = ['name', 'address_line', 'country', 'state', 'district', 'city', 'pincode',]


class CountryForm(forms.ModelForm):

    
    class Meta:
        model = Country
        # fields = ('__all__')
        fields = ['name', 'code', 'phone_code', 'currency_code',]

class StateForm(forms.ModelForm):

    
    class Meta:
        model = State
        # fields = ('__all__')
        fields = ['country', 'state', ]

class DistrictForm(forms.ModelForm):

    
    class Meta:
        model = District
        # fields = ('__all__')
        fields = ['state', 'district', ]
