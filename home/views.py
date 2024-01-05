from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
# appname/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'NonAuthenticated/index.html')

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
