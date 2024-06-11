from django.shortcuts import render
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy

# Create your views here.

# login view it's direct with path

# signup view
class UserSignUpView(CreateView):
    template_name = 'signup.html'
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')