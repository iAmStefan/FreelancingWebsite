from django import forms
from . import models

class ContactForm(forms.Form):
    name = forms.CharField(label='Name (mandatory)', max_length=100, required=True,
    widget=forms.TextInput(attrs={'class' : "input_name"}))
    email = forms.EmailField(label='E-mail (mandatory)', max_length=100, required=True,
    widget=forms.TextInput(attrs={'class' : "input_email"}))
    subject = forms.CharField(label='Subject (mandatory)', max_length=100, required=True,
    widget=forms.TextInput(attrs={'class' : "input_subject"}))
    reclamationReason = forms.CharField(label='Message (mandatory)', max_length=255, required=True,
    widget=forms.Textarea(attrs={'class' : "input_message"}))
