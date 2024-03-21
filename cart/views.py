from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,HttpResponse
from product.models import product
from .models import Cart,CartItem

# Create your views here.

def add_to_cart(request,productId):
    #logic of cart

    products=get_object_or_404(product,id=productId)
    print(products.product_name)

    #Fetching current User
    currentUser=request.user

    cart,created= Cart.objects.get_or_create(user=currentUser)

    print(created)

    item,item_created= CartItem.objects.get_or_create(cart=cart,produts=products)

    quantity=request.GET.get("quantity")

    if  not item_created:
        item.quantity+=int(quantity)

    else:
        item.quantity=1

    item.save()

    return HttpResponseRedirect("/pro/product/")

#===========================================================================
                                  # view cart
#===========================================================================
def view_cart(request):
    currentUser=request.user
    cart,created=Cart.objects.get_or_create(user=currentUser)
    cartItems=cart.cartitem_set.all()
    print(cartItems)
    finalAmount=0


    for item in cartItems:
        finalAmount+=item.quantity*item.produts.product_price


    return render(request,"cart.html",{"items":cartItems,"finalAmount":finalAmount})

#============================================================================
                               #update cart
#============================================================================

def update_cart(request,cartItemId):
    cartItem=get_object_or_404(CartItem,pk=cartItemId)
    quantity=request.GET.get("quantity")
    cartItem.quantity=int(quantity)
    cartItem.save()

    return HttpResponseRedirect("/cart/")

#============================================================================
                               #Delete cart item
#============================================================================

def delete_cart(request,cartItemId):
    cartItem=get_object_or_404(CartItem,pk=cartItemId)
    cartItem.delete()

    return HttpResponseRedirect("/cart/")

#===================================================
#            CHECKOUT
#===================================================

from .forms import OrderForm
from .models import Order,OrderItem
import uuid

def check_out(request):

    currentUser=request.user

    initial={
        "user":currentUser.get_username(),
        "first_name":currentUser,
        "last_name":currentUser


    }

    form=OrderForm(initial=initial)
    cart,created=Cart.objects.get_or_create(user=currentUser)
    cartItems=cart.cartitem_set.all()
    print(cartItems)
    finalAmount=0


    for item in cartItems:
        finalAmount+=item.quantity*item.produts.product_price

    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            user=request.user
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            address=form.cleaned_data['address']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            pincode=form.cleaned_data['pincode']
            phoneno=form.cleaned_data['phoneno']

            OrderId=str(uuid.uuid4())


        order=Order.objects.create(user=user,
                             first_name=first_name,
                             last_name=last_name,
                             address=address,
                             city=city,
                             state=state,
                             pincode=pincode,
       
                             phoneno=phoneno,
                             order_id=OrderId[:8])
        
        for item in cartItems:
            OrderItem.objects.create(order=order,
                                     produts=item.produts,
                                     quantity=item.quantity,
                                     total=item.quantity*item.produts.product_price)


        return HttpResponseRedirect("/payment/"+ OrderId[:8])    

    return render(request,"checkout.html",{"form":form,"items":cartItems,"finalAmount":finalAmount})

#===================================================
#           * MAKE PAYMENT *                       #
#===================================================

import razorpay

def make_payment(request,OrderId):
   # print(OrderId)
    order=Order.objects.get(pk=OrderId)
    orderItems=order.orderitem_set.all()
    amount=0

    for item in orderItems:
        amount+=item.total

    print(amount)

    client = razorpay.Client(auth=("rzp_test_KLtJwJD93bD6a5", "bAo1kf5rlAYCRh4hm0fs2F9B"))
    data = { "amount": amount*100, "currency": "INR", "receipt": OrderId,"payment_capture":1 }
    payment = client.order.create(data=data)


    return render(request,"payment.html",{"payment":payment})

#===================================================
#           * MAKE PAYMENT *                       #
#===================================================
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

@csrf_exempt
def success(request,OrderId):
    if request.method=="POST":
        client = razorpay.Client(auth=("rzp_test_KLtJwJD93bD6a5", "bAo1kf5rlAYCRh4hm0fs2F9B"))
        check=-client.utility.verify_payment_signature({
                      'razorpay_order_id': request.POST.get("razorpay_order_id"),
                      'razorpay_payment_id': request.POST.get("razorpay_payment_id"),
                      'razorpay_signature': request.POST.get("razorpay_signature"),
                    })
        if check:
            order=Order.objects.get(pk=OrderId)
            order.paid=True
            order.save()
            cart=Cart.objects.get(user=request.user)
            OrderItems=order.orderitem_set.all()
            send_mail(
                "Order Placed...",#sunject
                "",#,message
                settings.EMAIL_HOST_USER,
                ["sachinbalganeshan174@gmail.com","roushanshaikh040403@gmail.com"],
                fail_silently=False,
                html_message=render_to_string("email.html",{"items":OrderItems}))
            

            
            cart.delete()
           


            return render (request,"success.html",{})



   