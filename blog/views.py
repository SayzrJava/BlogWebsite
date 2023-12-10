# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blogs.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blogdetails.html', {'post': post})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})
