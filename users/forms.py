# users/forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'dob_gregorian': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'dob_ethiopian': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'passport_issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'passport_expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'your_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'grandfather_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
