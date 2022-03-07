from django.shortcuts import render

from .models import Group, Post

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts\index.html', context)


def group_posts(request, slug):
    context = {
        'slug': slug,
    }
    return render(request, 'posts\group_list.html', context)
