"""
URL configuration for focus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from intro import views as intro_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('',include('intro.urls')),
    path('admin/', admin.site.urls),
     path('accounts/', include('django.contrib.auth.urls')),
    path(' accounts/register/', intro_views.register, name='register'),
    path('', intro_views.home, name='home'),
    path('select_solar_needs/', intro_views.select_solar_needs, name='select_solar_needs'),
    path('purchase_confirmation/', intro_views.purchase_confirmation, name='purchase_confirmation'),
     path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html', 
        redirect_authenticated_user=True,
        success_url='/select_solar_needs/'  # Redirect to select_solar_needs page after login
    ), name='login'),
     path('company_panel/', intro_views.company_panel, name='company_panel'),
      path('intro/', include('intro.urls')),
     # path('payment_methods/', intro_views.payment_methods, name='payment_methods'),
      path('create_order/<int:panel_id>/', intro_views.create_order, name='create_order'),
      path('order_confirmation/', intro_views.order_confirmation, name='order_confirmation'),
    # path('checkout/', intro_views.checkout, name='checkout'),
      path('purchase/', intro_views.purchase, name='purchase'),
      path('mpesa_payment/', intro_views.mpesa_payment, name='mpesa_payment'),
    path('credit_card_payment/', intro_views.credit_card_payment, name='credit_card_payment'),
     path('contact/', intro_views.contact, name='contact'),
    path('about/', intro_views.about, name='about'),
    path('repair_request/',intro_views.repair_request_view,name='repair_request'),
    path('Batteries/',intro_views.batteries_view,name='Batteries'),
]    
