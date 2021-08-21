from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from products.models import Product
from .models import Order
from .forms import OrderForm

@login_required
def order_checkout_view(request):
    qs = Product.objects.filter(featured=True)
    if not qs.exists():
        return redirect("/")
    product = qs.first()
    user = request.user 
    order_id = request.session.get("order_id")
    order_obj = None
    new_creation = False
    try:
        order_obj = Order.objects.get(id=order_id)
    except:
        order_id = None
    if order_id == None:
        new_creation = True
        # 32:02 New Creation?
        order_obj = Order.objects.create(product=product, user=user)
    if order_obj != None and new_creation == False:
        if order_obj.product.id != product.id:
            order_obj = Order.objects.create(product=product, user=user)
    # ? 25:47
    request.session['order_id'] = order_obj.id
    form = OrderForm(request.POST or None, product=product, instance=order_obj)
    if form.is_valid():
        order_obj.shipping_address = form.cleaned_data.get("shipping_address")
        order_obj.billing_address = form.cleaned_data.get("billing_address")
        order_obj.save()
    return render(request, 'forms.html', {"form": form})

# def order_checkout_view(request):
#     qs = Product.objects.filter(featured=True)
#     if not qs.exists():
#         return redirect("/")
#     product = qs.first()
#     user = request.user # AnonUser
#     order_id = request.session.get("order_obj_id")
#     if order_id == None:
#         order_obj = Order.objects.create
#         Order.objects.create(product=product, user=user)
#         request.session['order_id'] = order_obj.id
#         order_obj = None
#         try:
#             order_obj = Order.objects.get(id=order_id)
#         except:
#             order_id = None
#     return render(request, 'forms.html', {})