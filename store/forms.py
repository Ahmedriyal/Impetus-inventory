from django import forms

from .models import Inventory, Purchase_Detail, Category


# ------ Categoty Form ------
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


# ------ Purchase Detail Form ------
class Purchase_DetailForm(forms.ModelForm):
    class Meta:
        model = Purchase_Detail
        fields = '__all__'


# ------ Inventory Form ------ 
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        
    # device_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'id': 'device_name',
    #     'data-val': 'true',
    #     'data-val-required': 'Please enter device name',
    # }))
    # company_or_user = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'id': 'company_or_user',
    #     'data-val': 'true',
    #     'data-val-required': 'Please enter Company or User',
    # }))
    # nos = forms.IntegerField(widget=forms.NumberInput(attrs={
    #     'class': 'form-control',
    #     'id': 'nos',
    #     'data-val': 'true',
    #     'data-val-required': 'Please enter Number',
    # }))
    # condition = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'id': 'condition',
    #     'data-val': 'true',
    #     'data-val-required': 'Please enter Condition',
    # }))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'class': 'form-control',
    #     'id': 'password',
    #     'data-val': 'true',
    #     'data-val-required': 'Please enter password',
    # }))
    # retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'class': 'form-control',
    #     'id': 'retype_password',
    #     'data-val': 'true',
    #     'data-val-required': 'Please enter retype_password',
    # }))
