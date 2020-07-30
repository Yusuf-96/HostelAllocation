from django import forms
from .models import Hostel

class HostelForm(forms.ModelForm):
    class Meta:
        model =Hostel
        exclude=['user']

        widgets={
            'name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'hostel name...',
                }
            ),
            'category':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
           
        }