from django import forms
from django.forms import TextInput, EmailInput

from .models import *




class ContactoForm(forms.Form):
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}), required=True)
    contact_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Tu email'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Asunto'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}), required=True)



class VideoNosForm(forms.ModelForm):
    class Meta:
        model= Nosotros
        fields= ["titulo","videofile"]


class VideoProForm(forms.ModelForm):
    class Meta:
        model= Proyecto
        fields= ["nombreProyecto","videofile"]
