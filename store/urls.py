from django.urls import path
from . import views
from store.controller import authview,cart,wishlist,checkout


urlpatterns=[

 path('', views.home,name="home"),
 path('collections', views.collections,name="collections"),
 path('collections/<str:slug>',views.collectionsview ,name="collectionsview"),
 path('collections/<str:cat_slug>/<str:prod_slug>', views.prodcutview ,name="prodcutview"),

 path('register/' ,authview.register,name="register"),
 path('login/' ,authview.loginpage,name="loginpage"),
 path('logout/' ,authview.logoutpage,name="logoutpage"),

path('add-to-cart' ,cart.addtocart,name="addtocart"),
path('cart',cart.viewCart,name="cart"),
path('update_card',cart.update_card,name="update_card"),
path('delete-card-item',cart.deletecarditem,name="delete-card-item"),

path('wishlist',wishlist.wish,name="wishlist"),
path('add-to-wishlist',wishlist.addtowishlist,name="add-to-wishlist"),
path('delete-wish-item',wishlist.deletewishitem,name="delete-wish-item"),

path('checkout',checkout.checkorder,name="checkout"),
path('palceorder',checkout.palceorder,name="palceorder"),

path('proced-to-pay',checkout.procedtopay,name="proced-to-pay"),








]
 