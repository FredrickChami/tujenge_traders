# appname/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
    path('', views.index, name='index'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),
    path('terms-and-conditions', views.terms_and_conditions, name='terms-and-conditions'),
]
