from django import forms
from django.forms import ModelForm
from .models import *

class taskForm(forms.ModelForm):
    #name = forms.CharField(widget= forms.TextInput(attrs={'placeholder' : 'Yangi topshiriq'}))
    #prioritet = forms.EmailField(widget= forms.NumberInput(attrs={'placeholder' : 'Topshiriq prioriteti'}))

    class Meta:
        model = task
        fields = '__all__'