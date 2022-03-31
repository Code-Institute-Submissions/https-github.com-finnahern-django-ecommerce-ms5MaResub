from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Form class for the user login form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(forms.ModelForm):
    """Form class for the new user registration form"""
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password",
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd["password2"]


class NewsletterForm(forms.Form):
    """Form class for the newsletter signup form"""
    fields = forms.EmailField()

    class Meta:
        fields = ("email",)
