from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.b 

class CreateUser(generic.CreateView):
    success_url = reverse_lazy('homepage')
    form_class = UserCreationForm
    template_name = 'signup.html'