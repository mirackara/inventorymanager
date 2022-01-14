from django.shortcuts import render

from .models import InventoryModel


def addToSQL(request):
    itemSkuPOST = request.POST['itemSku']
    itemNamePOST = request.POST['itemName']
    itemAislePOST = request.POST['itemAisle']
    itemAmountPOST = request.POST['itemAmount']
    # If the user did not fill out any forms
    if itemNamePOST == '' or itemSkuPOST == '' or itemAislePOST == '' or itemAmountPOST == '':
        return
    # TODO : Collision Checking
    
    # Dict for Initial Data with field names as keys
    context = {}
    # add the dictionary during initialization
    form = InventoryModel(request.POST or None)
    context['form'] = form
    # New Inventory Model Instance
    model = InventoryModel(itemSKU=request.POST['itemSku'], itemName=request.POST['itemName'],
                           itemAmount=request.POST['itemAmount'],
                           itemAisle=request.POST['itemAisle'])
    # Save Model to DB
    model.save()
