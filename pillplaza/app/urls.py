from django.urls import path
from . import views
# import views

urlpatterns = [
    path('',views.home,name="home"),
    path('shop',views.shop,name="shop"),
    path('shop/<int:name>',views.shopcategory,name="shop"),
    path('product/<int:id>',views.productview,name="product"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('registration/',views.registerationpage),
    path('cart/',views.cartview,name="cart"),
    path('orders/',views.order),
    path('track/',views.track),
    path('adminstats/',views.stats),

    path('register/',views.register),
    path('verifyotp/',views.sendverifyotp),
    path('login/',views.makeuserlogin),
    path('getmail/',views.getmail),
    path('forgot/<str:email>/<str:code>',views.resetpassword),
    path('add/to/cart',views.addToCart),
    path('updatecart/<str:str>/<int:productid>/<int:cartid>',views.updatecart),
    path('apply/cart',views.approveCart),
    path('delTemp/<int:id>',views.delTemperary),
    path('addtotop/<int:id>',views.addtotop),
    path('conformorder',views.conformOrder),
    path('conformorderotp/',views.conformOrderotp),
    path('makepayment/',views.makepayment,name="makepayment"),
    path('addorder/',views.addorder),
    path('thankyou/',views.thankyouorder,name="thankyou"),
    path('cancel/',views.cancelorder),
    path('update/refund',views.updaterefund),
    path('invoice/<str:orderid>',views.invoice),
    path('logout/',views.logoutuser),
    path('guestreg/',views.guestreg),
    path('guestsuccess/',views.guestsuccess,name="guestsuccess"),
    path('permit/<str:gtid>',views.permitgt),
    path('guest/<str:action>/<str:gtid>',views.guestaction),
    path('personalinfo/',views.personalinfo),
        

]
