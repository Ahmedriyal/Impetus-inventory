from multiprocessing import Condition
# from unicodedata import category
from django.db import models
from users.models import User


# ------ Category Model -------
class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.category_name


# ------ Inventory Model -------
class Inventory(models.Model):
    Condition_Choice = (
        ('New', 'New'),
        ('Used', 'Used'),
        ('Damaged', 'Damaged'),
    )

    Company_Choice = (
        ('Impetus Center', 'Impetus Center'),
        ('Impetus Office', 'Impetus Office'),
        ('Impetus Lounge', 'Impetus Lounge'),
        ('BMS', 'BMS'),
    )

    device_name = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    company_or_user = models.CharField(max_length=200, choices=Company_Choice)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    condition =  models.CharField(max_length=10, choices=Condition_Choice)
    note = models.CharField(max_length=990, null=True, blank=True)

    def __str__(self):
        return self.device_name


# ------ Purchase Detail Model -------
class Purchase_Detail(models.Model):
    item_name = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    unit_price = models.IntegerField(null=True, blank=True, default=0)
    purchased_by =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    purchased_from = models.CharField(max_length=500, null=True, blank=True)
    purchase_date = models.DateField()
    # created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name

    @property
    def get_total(self):
        
        total = self.unit_price * self.quantity
        return total