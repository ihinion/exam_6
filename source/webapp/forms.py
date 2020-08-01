from django import forms
from django.forms import widgets


class EntryForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Name')
    mail = forms.EmailField(max_length=60, required=True, label='Email')
    text = forms.CharField(max_length=500, required=True, label='Text', widget=widgets.Textarea)
