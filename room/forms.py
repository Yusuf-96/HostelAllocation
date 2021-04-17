from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model =Room
        exclude=['user','is_taken','level']

        widgets={
            'hostel':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'name':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'capacity':forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
        }



