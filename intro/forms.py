from django import forms
from .models import SolarNeed, SolarProduct, SolarPanel, Order, RepairRequest

class SolarNeedForm(forms.ModelForm):
    class Meta:
        model = SolarNeed
        fields = ['name', 'description']

class SolarProductForm(forms.ModelForm):
    class Meta:
        model = SolarProduct
        fields = ['name', 'description', 'price', 'cleaning_cost', 'repair_cost', 'solar_need']

class SolarPanelForm(forms.ModelForm):
     class Meta:
        model= SolarPanel
        fields=['name','description','price','efficiency','warranty_period']
class OrderForm(forms.ModelForm):
      class Meta:
        model= Order
        fields=['panel_name','price','quantity']
      panel_name = forms.CharField(max_length=100)
      price = forms.DecimalField(max_digits=10, decimal_places=2)
      quantity = forms.IntegerField(min_value=1)

class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['panel_name', 'problem_description', 'battery_type']
        widgets = {
            'problem_description': forms.Textarea(attrs={'rows': 4}),
        }