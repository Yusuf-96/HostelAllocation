from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model =Department
        exclude=['user']

        widgets={
            
            'name':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            
        }