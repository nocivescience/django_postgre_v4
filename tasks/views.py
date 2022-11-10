from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home.html',)
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2f']:
            try:
                user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                return HttpResponse('good job')
            except:
                return HttpResponse('user already exists')
        return HttpResponse('hola a todos')