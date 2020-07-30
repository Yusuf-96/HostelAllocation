from django import forms
from .models import Allocate

class AllocateForm(forms.ModelForm):
    class Meta:
        model =Allocate
        exclude=['user','is_allocated']

        widgets={
            'room':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
        }