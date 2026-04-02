from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        send_mail(
            subject="Registration Confirmed",
            message=f"Hi {user.username},\n\nYour registration is confirmed. Welcome aboard!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=True,
        )
        login(request, user)
        return redirect("dashboard")
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("dashboard")
    return render(request, "accounts/login.html", {"form": form})


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("login")


@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")
