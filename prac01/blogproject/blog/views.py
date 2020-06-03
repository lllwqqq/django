from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, template_name='blog/index.html', context={
        'title': '我的博客',
        'welcome': '欢迎来到Aroma的博客首页！！！'
    })
