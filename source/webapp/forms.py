from django import forms
from django.forms import widgets


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find', widget=widgets.Input(attrs={'class': 'form-control'}))
