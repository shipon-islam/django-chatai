
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import User

# Create your views here.


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        avatar = request.FILES.get('avatar')
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        errors = {}
        if not name:
            errors['name'] = 'Name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        elif User.objects.filter(email=email).exists():
            errors['email'] = 'Email already exists.'
        if not password:
            errors['password'] = 'Password is required.'
        elif password != cpassword:
            errors['cpassword'] = 'Passwords do not match.'
        if errors:
            return render(request, 'signup.html', {'errors': errors, 'name': name, 'email': email})
        user = User.objects.create_user(
            name=name, avatar=avatar if avatar else 'avatar.png', email=email, password=password)
        user.save()
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')

    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.email}!")
            return redirect('home')
        else:
            messages.error(
                request, "Invalid username or password. Please try again.")
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect("/accounts/signin")
