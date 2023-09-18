from multiprocessing import Condition
from django.db import models


from users.models import User


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

    Category_Choice = (
        ('CPU', 'CPU'),
        ('EC10', 'EC10'),
        ('HDD', 'HDD'),
        ('IP Camera', 'IP Camera'),
        ('Keyboard', 'Keyboard'),
        ('Monitor', 'Monitor'),
        ('Mouse', 'Mouse'),
        ('PABX', 'PABX'),
        ('Pendrive', 'Pendrive'),
        ('Printer', 'Printer'),
        ('PoE Switch', 'PoE Switch'),
        ('RAM', 'RAM'),
        ('Router', 'Router'),
        ('SSD', 'SSD'),
        ('Tab', 'Tab'),
        ('UPS', 'UPS'),
        ('Other', 'Other'),
    )
    device_name = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=200, choices=Category_Choice, null=True, blank=True)
    company_or_user = models.CharField(max_length=200, choices=Company_Choice)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    condition =  models.CharField(max_length=10, choices=Condition_Choice)

    def __str__(self):
        return self.device_name


# ------ Purchase Detail Model -------
class Purchase_Detail(models.Model):
    Category_Choice = (
        ('CPU', 'CPU'),
        ('EC10', 'EC10'),
        ('HDD', 'HDD'),
        ('Ink', 'Ink'),
        ('IP Camera', 'IP Camera'),
        ('Keyboard', 'Keyboard'),
        ('Laptop', 'Laptop'),
        ('Mobile', 'Mobile'),
        ('Monitor', 'Monitor'),
        ('Mouse', 'Mouse'),
        ('PABX', 'PABX'),
        ('Pendrive', 'Pendrive'),
        ('Printer', 'Printer'),
        ('PoE Switch', 'PoE Switch'),
        ('RAM', 'RAM'),
        ('Router', 'Router'),
        ('SSD', 'SSD'),
        ('Tab', 'Tab'),
        ('Toner', 'Toner'),
        ('UPS', 'UPS'),
        ('Other', 'Other'),
    )
    Company_Choice = (
        ('Impetus Office', 'Impetus Office'),
        ('Impetus Lounge', 'Impetus Lounge'),
        ('Impetus Center', 'Impetus Center'),
    )

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=200, choices=Category_Choice, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    unit_price = models.IntegerField(null=True, blank=True, default=0)
    purchased_by =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    purchased_from = models.CharField(max_length=500, null=True, blank=True)
    purchased_for = models.CharField(max_length=200, choices=Company_Choice, null=True, blank=True)
    purchase_date = models.DateField()
    # image = models.ImageField(upload_to='img/', null=True, blank=True)
    receipt = models.FileField(upload_to="receipt/", null=True, blank=True)
    # created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name

    @property
    def get_total(self):
        
        total = self.unit_price * self.quantity
        return total