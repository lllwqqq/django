from django.shortcuts import render,get_object_or_404,HttpResponse
from django.views.decorators.http import require_POST


# Create your views here.
from .forms import UserInfoForm
from .models import UserInfo


# @require_POST
def liuyan(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('信息提交成功')
        else:
            return '提交的信息有误'
    else:
        form = UserInfoForm()
        return render(request,template_name='formtest/formtest.html',context={
            'form': form
        })
