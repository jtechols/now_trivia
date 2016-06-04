from django import forms
from .models import *
from django.forms import ModelForm, CheckboxInput, Select

class CreateGame(ModelForm):
    class Meta:
        model = Game
        fields = ['rounds', 'show_title', 'show_artist']
        widgets = {
            'rounds': Select,
            'show_title': CheckboxInput,
            'show_artist': CheckboxInput,
        }
