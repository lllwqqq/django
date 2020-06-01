from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, template_name='index.html', context={})
        else:
            return render(request, template_name='login.html', context={})
    elif request.method == 'GET':
        return render(request, template_name='login.html', context={})
