from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
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

class NewPost(CreateView):
    model = Post
    template_name = 'post.html'
    fields = '__all__'

class Edit_post(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']

class Delete_post(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('homepage')
    
