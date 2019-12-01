from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Tag
import markdown
import re


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions={
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    })
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, template_name='blog/detail.html', context={
        'post': post
    })

def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month).order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'post_list': post_list
    })


def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=category).order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'post_list': post_list
    })


def tags(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'post_list': post_list
    })
