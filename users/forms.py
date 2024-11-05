# users/forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['your_name', 'father_name', 'grandfather_name', 'email', 'sex', 'phone_number']
        widgets = {
            'sex': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female')]),
        }
