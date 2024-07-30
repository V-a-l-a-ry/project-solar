from django.urls import path
from .import views

urlpatterns= [
    path('',views.homepage, name='homepage'),
    path('register/',views.register, name='register'),
    path('login/',views.login_user, name='login'),
    path('select_solar_needs/',views.select_solar_needs, name='select_solar_needs'),
    path('home_solar_panel_info/', views.home_solar_panel_info, name='home_solar_panel_info'),
    path('purchase/', views.purchase, name='purchase'),
   # path('payment_methods/', views.payment_methods, name='payment_methods'),
    path('mpesa_payment/', views.mpesa_payment, name='mpesa_payment'),
    path('credit_card_payment/', views.credit_card_payment, name='credit_card_payment'),
    path('process_payment/', views.credit_card_payment, name='process_payment'),
    path('company_panel/', views.company_panel, name='company_panel'),
    path('purchase_confirmation/', views.purchase_confirmation, name=' purchase_confirmation'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('create_order/<int:panel_id>/', views.create_order, name='create_order'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    #path('checkout/', views.checkout, name='checkout'),
     path('purchase/', views.purchase, name='purchase'),
     path('repair_request/',views.repair_request_view, name='repair_request'),
     path('Batteries/',views.batteries_view, name='Batteries'),
]   


    