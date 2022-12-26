from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from store.models import Product,Cart,Wishlist

@login_required(login_url='loginpage')
def wish(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlist}
    return render(request,"store/wishlistitem.html",context)



def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id')) 
            product_cheak=Product.objects.get(id=prod_id)
            if (product_cheak):
                if(Wishlist.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"product already in Wishlist "})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':"product added succssfully"})
            else:
                return JsonResponse({'status':"no such product found"})   
        else:
            return JsonResponse({'status':"login to continue"})
    return redirect('/')


def deletewishitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            if (Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                wishitem = Wishlist.objects.get(product_id=prod_id,user=request.user)
                wishitem.delete()
                return JsonResponse({'status':"product removed from wishlist"})
            else:
                    return JsonResponse({'status':"product not found in wishlist"})
        else:
                return JsonResponse({'status':"login to continue"})
            
    return redirect('/')