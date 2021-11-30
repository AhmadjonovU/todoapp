from django.db import models
from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','matn','time']