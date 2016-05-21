from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth

# Create your views here.
def sign_in(request):
    return render(request,'sign-in.html',{'var': 1})

def auth_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home.html')
    else:
        return render(request,'sign-in.html',{'var': 0})
    
def sign_up(request):
    render (request,'sign-up.html')
        
        