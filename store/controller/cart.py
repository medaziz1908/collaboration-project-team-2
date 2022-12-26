from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from store.models import Product,Cart

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            
            product_cheak=Product.objects.get(id=prod_id)
            if (product_cheak):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"product already in cart"})
                else:
                    prod_qty= int(request.POST.get('product_qty'))
                    if product_cheak.quantity>=prod_qty :
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"product added succssfully"})
                    else:
                         return JsonResponse({'status':"Only\t"+str(product_cheak.quantity)+"\tquantity avilable"}) 
            else:
                return JsonResponse({'status':"no such product found"})
        else:

            return JsonResponse({'status':"login to contnue"})

    return redirect('/')

@login_required(login_url='loginpage')
def viewCart(request):
    cart = Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,"store/cart.html",context)


def update_card(request):
    if request.method == 'POST':
        prod_id=int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty= int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty=prod_qty
            cart.save()
        return JsonResponse({'status':"update done"})
            
            
    return redirect('/')

def deletecarditem(request):
    if request.method == 'POST':
        prod_id=int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
            return JsonResponse({'status':" product deleted"})
    return redirect('/')