
import email
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .filters import PurchaseFilter, InventoryFilter
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime
from .decorators import auth_users, allowed_users

from users.models import User
from .models import (
    Purchase_Detail,
    Inventory,
)

from .forms import (
    Purchase_DetailForm,
    InventoryForm,
)



# ------ Purchase Detail View ------
def Purchase(request):
    if request.method == 'POST':
            form = Purchase_DetailForm(request.POST)
            if form.is_valid():
                purchasedetail = form.save(commit=False)
                purchasedetail.save()

                return redirect('purchase-list')
    else:
        form = Purchase_DetailForm()

    

    context = {'form': form}
    return render(request, 'store/purchase.html', context)
    

# ------ Purchase List View ------
def PurchaseListView(request):
    purchase = Purchase_Detail.objects.all().order_by('-purchase_date')

    purchase_filter = PurchaseFilter(request.GET, queryset=purchase)
    purchase = purchase_filter.qs
    
    context = {'purchase': purchase, 'purchase_filter': purchase_filter}
    return render(request, 'store/purchase_list.html', context)


# ------ Purchase PDF Generate View ------
def purchase_pdf_create(request):
    purchase = Purchase_Detail.objects.all().order_by('-purchase_date')

    purchase_filter = PurchaseFilter(request.POST, queryset=purchase)
    purchase = purchase_filter.qs

    template_path = 'store/purchasePdfReport.html'

    context = {'purchase': purchase, 'purchase_filter': purchase_filter}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="purchaselist.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# ------ Inventory View ------
@login_required(login_url='login')
def create_inventory(request):
    forms = InventoryForm()
    if request.method == 'POST':
        forms = InventoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            # device_name = forms.cleaned_data['device_name']
            # company_or_user = forms.cleaned_data['company_or_user']
            # nos = forms.cleaned_data['nos']
            # condition = forms.cleaned_data['condition']
            # password = forms.cleaned_data['password']
            # retype_password = forms.cleaned_data['retype_password']
            # if password == retype_password:
            #     user = User.objects.create_user(
            #         username=username, password=password,
            #         email=email, is_supplier=True
            #     )
            # Inventory.objects.create(device_name=device_name, company_or_user=company_or_user, nos=nos, condition=condition)
            return redirect('inventory-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_inventory.html', context)


# ------ Inventory List View ------
def InventoryListView(request):
    inventory = Inventory.objects.all().order_by('device_name')

    inventory_filter = InventoryFilter(request.GET, queryset=inventory)
    inventory = inventory_filter.qs

    context = {'inventory': inventory, 'inventory_filter': inventory_filter}
    return render(request, 'store/inventory_list.html', context)


# ------ Inventory Item Edit View ------
@login_required(login_url='login')
# @allowed_users(allowed_roles=['Admin'])
def inventory_edit(request, pk):
    item = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory-list')
    else:
        form = InventoryForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'store/inventory_edit.html', context)


# ------ Inventory Item Delete View ------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def inventory_delete(request, pk):
    item = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory-list')
    context = {
        'item': item
    }
    return render(request, 'store/inventory_delete.html', context)


# ------ Inventory PDF Generate View ------
def pdf_report_create(request):
    inventory = Inventory.objects.all().order_by('device_name')

    inventory_filter = InventoryFilter(request.GET, queryset=inventory)
    inventory = inventory_filter.qs

    template_path = 'store/pdfReport.html'

    context = {'inventory': inventory, 'inventory_filter': inventory_filter}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="inventory.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response