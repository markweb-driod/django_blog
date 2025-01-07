from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class Homepage(ListView):
    model = Post
    template_name = 'homepage.html'

class About(ListView):
    model = Post
    template_name = 'about.html'

class Details(DetailView):
    model = Post
    template_name = 'content.html'