from django import forms
from django.forms import widgets
from .models import Publication


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find', widget=widgets.Input(attrs={'class': 'form-control'}))


class PublicationForm(forms.ModelForm):

    class Meta:
        model = Publication
        fields = ('content', 'img', )
        error_messages = {
            'content': {
                'required': 'Please enter title',
            }
        }
