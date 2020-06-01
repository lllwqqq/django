from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


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
        TocExtension(slugify=slugify)
    })
    post.body = md.convert(post.body)
    post.toc = md.toc
    return render(request, template_name='blog/detail.html', context={
        'post': post
    })


def archive(request,year,month):
    post_list = Post.objects.filter(create_time__year=year,create_time__month=month).order_by('-create_time')
    return render(request,template_name='blog/index.html',context={
        'post_list': post_list
    })


def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request,template_name='blog/index.html',context={
        'post_list': post_list
    })


def tag(request,pk):
    tag = get_object_or_404(Tag,pk=pk)
    post_list = Post.objects.filter(tags=tag).order_by('-create_time')
    return render(request,template_name='blog/index.html',context={
        'post_list': post_list
    })