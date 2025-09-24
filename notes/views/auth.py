from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from notes.validation.auth_validation import RegisterValidation, LoginValidation


def register_view(request):
    if request.method == "POST":
        form = RegisterValidation(request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username=username, password=password,email=email)
            login(request, user)
            return redirect("login")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect("register")
    else:
        form = RegisterValidation()
    return render(request, "auth/register.html", {"form": form})


def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect("notes:note_index")
    if request.method == "POST":
        form = LoginValidation(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("notes:note_index")
            else:
                messages.error(request, "Username atau password salah")
                return redirect("login")
    else:
        form = LoginValidation()

    return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
