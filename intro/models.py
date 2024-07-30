from django.db import models
from django.contrib.auth.models import User

class SolarNeed(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class SolarProduct(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cleaning_cost = models.DecimalField(max_digits=10, decimal_places=2)
    repair_cost = models.DecimalField(max_digits=10, decimal_places=2)
    solar_need = models.ForeignKey(SolarNeed, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    panel_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f"Order for {self.panel_name} - {self.quantity} units"
    
class SolarPanel(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField(blank=True, null=True)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     efficiency = models.DecimalField(max_digits=5, decimal_places=2)
     warranty_period = models.PositiveIntegerField()  # Warranty in years
     

     def __str__(self):
        return self.name
class Meta:
        verbose_name = "Solar Panel"
        verbose_name_plural = "Solar Panels"


class RepairRequest(models.Model):
    panel_name = models.CharField(max_length=255)
    problem_description = models.TextField()
    battery_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.panel_name
class Battery(models.Model):
    name = models.CharField(max_length=255)
    panel_match = models.CharField(max_length=255)  # A field to specify the compatible panel
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"
# Create your models here.
