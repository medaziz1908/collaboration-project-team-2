import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from store.models import Product,Cart,Order,OrderItem,Profile
from django.contrib import messages
from django.contrib.auth.models import User



@login_required(login_url='loginpage')
def checkorder(request):
    
    rowcart=Cart.objects.filter(user=request.user.id)
    for item in rowcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cratitems=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cratitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    userprofile=Profile.objects.filter(user=request.user).first()

    context= {'cratitems':cratitems,'total_price':total_price,'userprofile':userprofile}   
    return render (request,"store/checkout.html",context) 



@login_required(login_url='loginpage')
def palceorder(request):
    if request.method == 'POST':
        currentuser=User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name=request.POST.get('fname')
            currentuser.last_name=request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user).first():
            userprofile=Profile()
            userprofile.user=request.user
            userprofile.phone=request.POST.get('phone')
            userprofile.address=request.POST.get('addresse')
            userprofile.city=request.POST.get('city')
            userprofile.state=request.POST.get('state')
            userprofile.country=request.POST.get('country')
            userprofile.pincode=request.POST.get('pin_code')
            userprofile.save()


        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.address=request.POST.get('addresse')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.country=request.POST.get('country')
        neworder.pincode=request.POST.get('pin_code')
        neworder.payment_mode=request.POST.get('payment_mode')

        cart=Cart.objects.filter(user=request.user)
        cart_total_price=0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
        
        neworder.total_price =cart_total_price

        trackno='order_'+str(random.randint(1111111,9999999))   
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno='order_'+str(random.randint(1111111,9999999))  
        neworder.tracking_no=trackno
        neworder.save()

        neworderitems=Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price = item.product.selling_price * item.product_qty,
                quantity = item.product_qty
            )
            # decrress stock qty
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()
        # clear user's cart
        Cart.objects.filter(user=request.user).delete()
        messages.success(request,"your order has been placed succssfully")

    return redirect('/')


@login_required(login_url='loginpage')
def procedtopay (request):
    cart = Cart.objects.filter(user=request.user)
    total_price=0
    for item in cart:
        total_price = total_price + item.product.selling_price * item.product_qty

    return JsonResponse({'total_price':total_price})
