from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render,get_object_or_404
from cards.models import Detail
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect
import random
from user.models import User
# def checkout(request):
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data

#             request.session['order_id'] = o.id
#             return redirect('process_payment')


#     else:
#         form = CheckoutForm()
#         return render(request, 'ecommerce_app/checkout.html', locals())

def process_payment(request):
    # order_id = Detail.objects.filter(email=request.session['username']).last().id
    # details = Detail.objects.filter(email = User.objects.filter(id=request.user.id).first().email).last()
    # details = get_object_or_404(Detail, id=order_id)
    host = request.get_host()
    paypal_dict = {
           "business": "sb-srs8h26410837@business.example.com",
        "amount": "10.00",
        "item_name": "name of the item",
        "invoice": "unique"+str(random.randint(1,1000000)),
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri( reverse('payment:payment_done')),
        "cancel_return": request.build_absolute_uri(reverse('payment:payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypal/process_payment.html', {'form': form})

@csrf_exempt
def payment_done(request):
    details = Detail.objects.filter(email = request.session['username']).last()
    user = User.objects.get(username=request.session['username'])
    user.paid_member = True
    user.save()
    messages.success(request,'Payment Successful')
    user = User.objects.get(username=request.session['username'])
    return render(request,'cards/generate.html',{'username':request.session['username'],'details':details,'id':details.id,'theme':1})


@csrf_exempt
def payment_canceled(request):
    details = Detail.objects.filter(email=request.session['username']).last()
    messages.error(request,'Payment Cancelled')
    return render(request,'cards/generate.html',{'username':request.session['username'],'details':details,'id':details.id,'theme':1})

