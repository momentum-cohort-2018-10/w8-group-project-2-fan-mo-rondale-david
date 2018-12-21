from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from questions.forms import EditProfileForm


def index(request):
    return render(request, 'index.html')


def register(request):
    """
    Redirects to home page upon successful user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'registration_form.html', {
            'form': form
        })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('account_home')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {
            'form': form
        })

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        
        args = {'form': form}
        return render(request, 'registration/change_password.html', args)