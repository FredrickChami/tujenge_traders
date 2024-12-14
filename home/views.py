from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from inventory_management.models import Product,PurchaseOrderRequest
import sweetify
from django.core.mail import send_mail
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
# from django.contrib.sessions.backends.base import UpdateDictMixin

def index(request):
    return render(request, 'NonAuthenticated/index.html')

def create_order(request):
    products = Product.objects.filter(quantity__gte=0).all()
    return render(request, 'NonAuthenticated/create-order.html',{'products':products})

def contact_us(request):
    return render(request, 'NonAuthenticated/contact-us.html')

def submit_information(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        # ConctactUsDetails.objects.create(
        #     customer_name = name,
        #     customer_email = email,
        #     customer_phone = phone,
        #     description = description
        # )

        subject = 'Customer contacted You'
        html_content = '<b>Customer Details</b><br/>'+'<b>Name:</b> '+ name +'<br/><b>Email:</b> '+email+'<br/><b>Phone No.:</b> '+phone+'<br/><br/><b>Order Details:</b><br/>'+description

        msg = EmailMultiAlternatives(subject,html_content, email if email else 'system@tujengetraders.com', ['info@tujengetraders.com'])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


        if email:
            html_content_customer = 'Mpendwa '+name+',<br/><br/>Oda yako yenye Taarifa zifuatazo imepokelewa kikamilifu, na tutakurudia haraka iwezekanavyo.'+'<br/><br/><b>Taarifa za Oda:<br/></b> '+description+'<br/><br/>Wako Mwaminifu katika Ujenzi,<br/>Tujenge Traders.'
            msg = EmailMultiAlternatives('Oda Kupokelewa Kikamilifu',html_content_customer, 'system@tujengetraders.com', [email])
            msg.attach_alternative(html_content_customer, "text/html")
            msg.send()

        sweetify.toast(request, 'Wasilisho lako limepokelewa kikamilifu!, Tutakurudia Haraka Iwezekanavyo. Jenga na Tujenge Traders.', icon="success", timer=10000, position="bottom")
        return redirect('/contact-us')
    
    sweetify.error(request, 'Samahani!,Imeshindikana kuwasilisha Taarifa zako, tafadhali jaribu njia mbadala kama kupiga simu ama kufika ofisini kwetu.', button="Sawa!", persistent=True)
    return redirect('/contact-us')

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

        # subject = 'New Purchase Order Request'
        # html_content = '<b>Customer Details</b><br/>'+'<b>Name:</b> '+ name +'<br/><b>Email:</b> '+email+'<br/><b>Phone No.:</b> '+phone+'<br/><br/><b>Order Details:</b><br/>'+description

        # msg = EmailMultiAlternatives(subject,html_content, email if email else 'info@tujengetraders.com', ['info@tujengetraders.com'])
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()


        # if email:
        #     html_content_customer = 'Mpendwa '+name+',<br/><br/>Oda yako yenye Taarifa zifuatazo imepokelewa kikamilifu, na tutakurudia haraka iwezekanavyo.'+'<br/><br/><b>Taarifa za Oda:<br/></b> '+description+'<br/><br/>Wako Mwaminifu katika Ujenzi,<br/>Tujenge Traders.'
        #     msg = EmailMultiAlternatives('Oda Kupokelewa Kikamilifu',html_content_customer, 'info@tujengetraders.com', [email])
        #     msg.attach_alternative(html_content_customer, "text/html")
        #     msg.send()

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

def add_to_cart(request):
    session = request.session
    product_id= request.POST['product_id']
    quantity= request.POST['quantity']
    cart_items = session.get('cart_items', [])  # Get existing cart items or create an empty list

    existing_item = next((item for item in cart_items if item['product_id'] == product_id), None)
    if existing_item:
        existing_item['quantity'] += quantity
    else:
        cart_items.append({'product_id': product_id, 'quantity': 1})

    session['cart_items'] = cart_items
    session.save()  # Update the session data (required for UpdateDictMixin)
    print(session['cart_items'])
    return redirect('cart_view')  # Redirect to the cart view

def remove_from_cart(request, product_id):
    session = request.session

    cart_items = session.get('cart_items', [])  # Get existing cart items or create an empty list

    existing_item = next((item for item in cart_items if item['product_id'] == product_id), None)
    if existing_item:
        existing_item['quantity'] += 1
    else:
        cart_items.append({'product_id': product_id, 'quantity': 1})

    session['cart_items'] = cart_items
    session.save_modified()  # Update the session data (required for UpdateDictMixin)

    return redirect('cart_view')  # Redirect to the cart view

def cart_view(request):
    cart_items = request.session.get('cart_items', [])
    return cart_items