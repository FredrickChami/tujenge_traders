from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from inventory_management.models import Product,PurchaseOrderRequest
import sweetify
from django.core.mail import send_mail
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives


def index(request):
    return render(request, 'NonAuthenticated/index.html')

def create_order(request):
    products = Product.objects.filter(quantity__gte=0).all()
    return render(request, 'NonAuthenticated/create-order.html',{'products':products})

def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        PurchaseOrderRequest.objects.create(
            customer_name = name,
            customer_email = email,
            customer_phone = phone,
            description = description
        )

        subject = 'New Purchase Order Request'
        html_content = '<b>Customer Details</b><br/>'+'<b>Name:</b> '+ name +'<br/><b>Email:</b> '+email+'<br/><b>Phone No.:</b> '+phone+'<br/><br/><b>Order Details:</b><br/>'+description

        msg = EmailMultiAlternatives(subject,html_content, email if email else 'info@tujengetraders.com', ['info@tujengetraders.com'])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


        if email:
            html_content_customer = 'Mpendwa '+name+',<br/><br/>Oda yako yenye Taarifa zifuatazo imepokelewa kikamilifu, na tutakurudia haraka iwezekanavyo.'+'<br/><br/><b>Taarifa za Oda:<br/></b> '+description+'<br/><br/>Wako Mwaminifu katika Ujenzi,<br/>Tujenge Traders.'
            msg = EmailMultiAlternatives('Oda Kupokelewa Kikamilifu',html_content_customer, 'info@tujengetraders.com', [email])
            msg.attach_alternative(html_content_customer, "text/html")
            msg.send()

        sweetify.toast(request, 'Oda yako Imepokelewa kikamilifu!, Tutakurudia Haraka Iwezekanavyo. Jenga na Tujenge Traders.', icon="success", timer=10000, position="bottom")
        return redirect('/create-order')
    
    sweetify.error(request, 'Samahani!,Imeshindikana kuwasilisha Oda yako, tafadhali jaribu njia mbadala kama kupiga simu ama kufika ofisini kwetu.', button="Sawa!", persistent=True)
    return redirect('/create-order')

def privacy_policy(request):
    return render(request, 'NonAuthenticated/privacy-policy.html')

def terms_and_conditions(request):
    return render(request, 'NonAuthenticated/terms-and-conditions.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('bulk-sms')
    return render(request, 'NonAuthenticated/Authentication/login.html')

@login_required
def event(request):
    print(request.user)
    return render(request, 'Authenticated/event/events.html')

@login_required
def signout(request):
    logout(request)
    
    # Disconnect the social authentication
    return redirect('index')
