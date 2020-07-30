from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model =Course
        exclude=['user']

        widgets={
           
            'name':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'department':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
        }