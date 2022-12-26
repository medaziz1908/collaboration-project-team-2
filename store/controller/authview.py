from django.shortcuts import render, redirect
from urllib import request
from django.contrib import messages

from store.forms import customeruserform
from django.contrib.auth import authenticate,login,logout



def register(request):
    form = customeruserform()
    if request.method == 'POST':
        form = customeruserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"resister done successfully")
            return redirect('/login')
    context = {'form':form}
    return render (request,"store/auth/register.html",context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"you already logged in")
        return redirect('/')
    else:   
        if request.method == 'POST':
                name = request.POST.get('username')
                passwd = request.POST.get('password')

                user = authenticate(request, username=name,password=passwd)
                if user is not None:
                    login(request,user)
                    messages.success(request,"logged in successfuly")
                    return redirect('/')
                else:
                    messages.error(request,"invald user or password")
                    return redirect('/login')

        return render (request,"store/auth/login.html")


def logoutpage (request):
     if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged Out successfuly")
        return redirect('/')


