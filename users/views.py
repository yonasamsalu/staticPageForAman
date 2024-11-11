from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

# users/views.py
from django.shortcuts import render, redirect
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/register.html', {'form': form})
    else:
        form = UserForm()

    return render(request, 'users/register.html', {'form': form})

# users/views.py
def home(request):
    return render(request, 'users/home.html')
