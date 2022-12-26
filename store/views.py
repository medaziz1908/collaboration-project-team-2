from urllib import request
from django.shortcuts import render, redirect
from .models import Category,Product,Cart
from django.contrib import messages
from django.http import JsonResponse




# Create your views here.

def home (request):
    return render (request,"store/index.html")

def collections (request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render (request,"store/collections.html",context)
    

def collectionsview (request , slug):
    if (Category.objects.filter(slug=slug, status=0)):
        Products = Product.objects.filter(category__slug = slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'Products':Products,'category':category}
        return render (request,"store/products/index.html",context)
    else: 
        messages.warning(request,"no such category found")
        return redirect('category')


def prodcutview (request,cat_slug,prod_slug)  :
    if (Category.objects.filter(slug=cat_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first

            context = {'products':products}

        else: 
         messages.warning(request,"no such category found")
         return redirect('collections')

    else: 
         messages.warning(request,"no such product found")
         return redirect('collections')

    return render (request,"store/Products/view.html",context) 

