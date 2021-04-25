from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm, LoginForm
from django.contrib.auth.models import  User

def register(request):
    if request.method == "POST":
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account creatded {form.cleaned_data['username']}")
            return redirect("login")
    else:
        form  = CreateUserForm()
    return render(request, "users/register.html", {"form" : form})



@login_required
def profile(request, profile_id):
    profile =  User.objects.get(id = profile_id)
    return  render(request, "users/profile.html", {"user" :  profile})



