# appname/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
    path('', views.index, name='index'),
    path('create-order', views.create_order, name='create_order'),
    path('submit-order', views.submit_order, name='submit_order'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),
    path('terms-and-conditions', views.terms_and_conditions, name='terms-and-conditions'),

    # Contact Us 
    path('contact-us', views.contact_us, name='contact_us'),
    path('submit-information', views.submit_information, name='submit_information'),
]
