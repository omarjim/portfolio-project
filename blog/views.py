from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    allblogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'allblogs': allblogs})

def detail(request, bloga_id):
    detailblog = get_object_or_404(Blog, pk=bloga_id)
    return render(request, 'blog/detailblog.html', {'blog': detailblog})
