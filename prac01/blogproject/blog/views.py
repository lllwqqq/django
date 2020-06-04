from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'post_list': post_list,
    })
