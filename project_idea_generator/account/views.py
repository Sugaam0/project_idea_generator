from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse, reverse_lazy
from account.forms import *
from django.db import IntegrityError

def registration(request):
    if request.user.is_authenticated:
        return redirect('idea_app:home')
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')

        # Basic validation
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Account/registration.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'Account/registration.html')

        user = User.objects.create_user(
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name,
            gender=gender  # only if gender is a field in your User model
        )

            # Optionally save gender to a profile model if you have one
            # Example:
            # Profile.objects.create(user=user, gender=gender)

        messages.success(request, "Your account has been successfully created. Please log in.")
        return redirect('account:login')

    return render(request, 'Account/registration.html')

def user_logIn(request):
    form = UserLoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return redirect('idea_app:home')
    context = {
        'form': form,
    }
    return render(request,'account/login.html',context)

def user_logOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You have Successfully logged out!')
    return redirect('account:login')

def employee_edit_profile(request, id):
    # your view logic here
    pass