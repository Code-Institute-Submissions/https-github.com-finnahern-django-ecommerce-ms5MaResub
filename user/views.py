from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . forms import LoginForm, UserRegistrationForm


def user_login(request):
    """
    Renders and authenticates the user login form
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(request,
                                username=cleaned_data["username"],
                                password=cleaned_data["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()

    template = "user/login.html"
    context = {"form": form}
    return render(request, template, context)
