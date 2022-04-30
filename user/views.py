from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from checkout.models import Order
from . forms import LoginForm, UserRegistrationForm


def user_login(request):
    """
    Renders and authenticates the user login form
    """
    if request.user.is_authenticated:
        return redirect(reverse("shop"))
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


def register(request):
    """
    Renders the registration page to create new user accounts.
    """
    if request.user.is_authenticated:
        return redirect(reverse("shop"))
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but don't save it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data["password"])
            # Save the user object
            new_user.save()
            # And log in the
            user = authenticate(request,
                                username=user_form.cleaned_data["username"],
                                password=user_form.cleaned_data["password"])
            login(request, user)

            return redirect("/")
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  "user/register.html",
                  {"user_form": user_form})


@login_required()
def order_history(request):
    """
    Renders the user's order history
    """

    orders = Order.objects.all()
    user_history = Order.objects.none()

    query = Q(user__exact=request.user.username)
    user_history = orders.filter(query)

    template = "user/order_history.html"
    context = {
        "user_history": user_history
    }

    return render(request, template, context)


def newsletter_signup(request):
    """
    Renders the newsletter sign up form
    """

    template = "user/newsletter.html"
    context = {}

    return render(request, template, context)
