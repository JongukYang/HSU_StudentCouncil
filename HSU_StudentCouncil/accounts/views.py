from django.shortcuts import render, redirect
from django.contrib import auth
from .models import UserProfile

# Create your views here.
def login(request):
    if request.method == 'POST':
        # form = LoginForm()
        _id = request.POST["username"]
        _pass1 = request.POST["password1"]
        _pass2 = request.POST["password2"]

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()