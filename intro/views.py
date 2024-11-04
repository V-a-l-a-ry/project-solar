from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import SolarNeed, SolarProduct, Order, SolarPanel,Battery 
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .forms import OrderForm, RepairRequestForm
import random
import string
#stripe.api_key = settings.STRIPE_SECRET_KEY

def select_solar_need(request):
    needs = SolarNeed.objects.all()
    return render(request, 'intro/select_solar_need.html', {'needs': needs})

def view_products(request, need_id):
    need = get_object_or_404(SolarNeed, pk=need_id)
    products = SolarProduct.objects.filter(solar_need=need)
    return render(request, 'intro/view_products.html', {'products': products, 'need': need})

def some_view(request):
    panels = SolarPanel.objects.all()
    return render(request, 'intro/view_products.html', {'panels': panels})

def home(request):
    return render(request,'home.html',{'name':'vall'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('select_solar_needs')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'intro/home.html')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('select_solar_needs')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'intro/login.html', {'form': form})

def select_solar_needs(request):
   selected_need = request.POST.get('solar_need')
   if request.method == 'POST':
        selected_need = request.POST.get('solar_need')
   if selected_need == 'home':
            return redirect('home_solar_panel_info')
   elif selected_need == 'company':
            return redirect('company_panel')
   elif selected_need=='repair':
            return  redirect('repair_request')
   elif selected_need=='batteries':
            return redirect('Batteries')
   return render(request, 'intro/select_solar_needs.html')
   return redirect('confirmation')  # Replace 'confirmation' with your actual URL name
    
   return render(request, 'intro/select_solar_needs.html')
   if request.user.is_authenticated:
        return render(request, 'intro/select_solar_needs.html')
   else:
        # Handle cases where user is not authenticated
        return redirect('login')
   
def purchase_confirmation(request):
    if request.method == 'POST':
        panel = request.POST.get('panel')
        payment_method = request.POST.get('payment_method')

        context = {
            'panel': panel,
            'payment_method': payment_method
        }
        return render(request, 'intro/purchase_confirmation.html', context)

    return redirect('select_solar_needs')


def home_solar_panel_info(request):
    # Add context data with information about home solar panels
   panels = [
        {
            'name': 'Panel A',
            'price': '$1000',
            'energy_output': '10 kW',
            'lifespan': '25 years'
        },
        {
            'name': 'Panel B',
            'price': '$1200',
            'energy_output': '12 kW',
            'lifespan': '30 years'
        },
        # Add more panels as needed
    ]

   context = {
        'panels': panels
    }
   return render(request, 'intro/home_solar_panel_info.html', context)
def home_solar_panel_info(request):
   # panels = SolarPanel.objects.all()
    return render(request, 'intro/home_solar_panel_info.html')
def company_panel(request):
 return render(request, 'intro/company_panel.html')

def purchase(request):
     # panel = get_object_or_404(SolarPanel, id=panel_id)   
  # if request.method == 'POST':
      #payment_method = request.POST.get('payment_method')
  
   #if payment_method == 'credit_card':
            # Redirect to Credit Card payment page
       #    return redirect('credit_card_payment')  # Adjust 'credit_card_payment' to your actual view name
  # else:
    
        # Handle GET request or other methods
      return redirect('order_confirmation')
    
#def payment_methods(request):
     # panel = request.GET.get('panel', 'None')
     #panel = get_object_or_404(SolarPanel, id=panel_id)
      #if request.method == "POST":
    
    # panel = request.GET.get('panel', 'None')
    
        # Process payment details here
      # return redirect('order_confirmation')
        
     # else:
       
    # return  render(request, 'payment_methods.html',{})

def mpesa_payment(request):
     # Logic to integrate with M-Pesa API
    # Redirect to the actual M-Pesa API endpoint
    mpesa_api_url = 'https://mpesa.api.url'
    return redirect(mpesa_api_url)

def credit_card_payment(request):
    # Implement credit card payment processing logic here
    if request.method == 'POST':
       card_name = request.POST.get('card_name')
       card_number = request.POST.get('card_number')
       expiry_date = request.POST.get('expiry_date')
       cvv = request.POST.get('cvv')
        
        # Process the payment here
        # If successful, redirect to a success page or render success message
        # If failure, redirect to a failure page or render failure message
   # return redirect('intro/payment_confirmation')

    
    return render(request, 'intro/credit_card_payment.html')

def payment_confirmation_view(request):
    return render(request, 'intro/payment_confirmation.html')
def company_panel(request):
    return render(request, 'intro/company_panel.html')
       
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # You can handle the message here, e.g., save to the database or send an email
        send_mail(
            subject=f'Message from {name}',
            message=message,
            from_email=email,
            recipient_list=[settings.ADMIN_EMAIL],
        )
        
        return HttpResponse('Thank you for your message.')
    
    return render(request, 'intro/contact.html')
def homepage(request):
    return render(request, 'intro/homepage.html')
def about(request):
    return render(request, 'intro/about.html')
def create_order(request, panel_id):
    panel = get_object_or_404(SolarPanel, id=panel_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.panel = panel
            order.save()
            return redirect('order_confirmation')
    else:
        form = OrderForm()
    return render(request, 'intro/create_order.html', {'form': form, 'panel': panel})

#def checkout(request):
  #  if request.method == 'POST':
   #     token = request.POST['stripeToken']
   #     total_amount = request.POST['total_amount']
    #    items = request.POST['items']

     #   try:
      #      charge = stripe.Charge.create(
      #          amount=int(float(total_amount) * 100),
       #         currency='usd',
        #        source=token,
       #         description='Solar Panel Purchase'
       #     )
    #        order_number = create_order()
      #      order = Order.objects.create(
         #       order_number=order_number,
          #      items=items,
           #     total_amount=total_amount
      #      )
          #  return redirect('order_confirmation', order_number=order_number)
     #   except stripe.error.StripeError as e:
      #      return render(request, 'intro/checkout.html', {'error': str(e)})

   # return render(request, 'intro/checkout.html', {'stripe_key': settings.STRIPE_PUBLISHABLE_KEY})



def order_confirmation(request):
     if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            panel_name = form.cleaned_data.get('panel_name')
            price = form.cleaned_data.get('price')
            quantity = form.cleaned_data.get('quantity')

            # Ensure the data is valid
            if panel_name is not None and price is not None and quantity is not None:
                # Save the order to the database
                Order.objects.create(panel_name=panel_name, price=price, quantity=quantity)
                return redirect('intro/order_confirmation.html')  # Redirect to a success page or similar
           # else:
                # Handle the case where data is missing or invalid
               # form.add_error(None, 'Error: Invalid form data.')
        #else:
            # Handle invalid form
           # form.add_error(None, 'Form is not valid.')
     else:
        form = OrderForm()

     return render(request, 'intro/order_confirmation.html', {'form': form}) 
def order_view(request):
    if request.method == "POST":
        # Process the order details here
        # For example, save the order to the database
        order = Order.objects.create(
            user=request.user,
            product_id=request.POST['product_id'],
            quantity=request.POST['quantity'],
            total_price=request.POST['total_price']
        )
        # Redirect to the payment page with the order ID
        return redirect('payment_methods', order_id=order.id)
    
    # If GET request, just render the order page
    return render(request, 'intro/create_order.html')
#def purchase(request, panel_id):
    # Redirect to create_order page with the panel_id
   # return redirect('create_order', panel_id=panel_id)
#def some_view(request):
  #  panel_id = 1  # Example panel_id
   # url = reverse('payment_methods', args=[panel_id])
def repair_request_view(request):
    if request.method == 'POST':
        form = RepairRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Batteries')  # Redirect to a success page or another page
    else:
        form = RepairRequestForm()
    
    return render(request, 'intro/repair_request.html', {'form': form})
def batteries_view(request):
    Batteries = Battery.objects.all()
    return render(request, 'intro/Batteries.html', {'Batteries': Batteries})