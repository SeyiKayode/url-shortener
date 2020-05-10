from django import forms
from .models import ShortURL


class UrlForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['long_url']
