from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request,template_name='blog/index.html',context={
        'post_list': post_list
    })
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,template_name='blog/detail.html',context={
        'post': post
    })
