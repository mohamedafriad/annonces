from django import forms
from .models import Message

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100, required=True)
    password = forms.CharField(label="password", max_length=200, required=True)

class ContactForm(forms.ModelForm):
    #nom = forms.CharField(label="nom", max_length=100, required=True)
    #email = forms.EmailField(label="email", max_length=200, required=True)
    #message = forms.CharField(label="Message", max_length=1000, required=True)

    class Meta:
        model = Message
        fields = '__all__'