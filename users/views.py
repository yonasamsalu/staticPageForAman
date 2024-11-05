# users/views.py
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Save the user data temporarily in session
            request.session['user_data'] = form.cleaned_data
            return redirect('password')  # Redirect to password page
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password:
            user_data = request.session.pop('user_data', None)
            if user_data:
                user = User(**user_data)
                user.save()
                messages.success(request, 'Registration successful!')
                return redirect('home')  # Redirect to the home page or any other page
    return render(request, 'password.html')
