
from django.contrib import admin
from . models import User
#from . import models
from .forms import UserForm  # Import the custom form

# Register your models here.


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['your_name', 'father_name', 'grandfather_name', 'sex','email', 'dob_ethiopian',
                    'dob_gregorian', 'phone_number', 'passport_number', 'passport_issue_date', 'passport_expiry_date']