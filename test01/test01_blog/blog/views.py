from django.shortcuts import render,get_object_or_404
from .models import Post
import markdown

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request,template_name='blog/index.html',context={
        'post_list': post_list
    })
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',]
    )
    post.body = md.convert(post.body)
    post.toc = md.toc

    return render(request,template_name='blog/detail.html',context={
        'post': post
    })
