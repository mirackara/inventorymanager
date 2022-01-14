from django.shortcuts import render
from inventoryApp.models import InventoryModel

def searchSQL(request):
    print(request.POST)
    itemSkuPOST = request.POST['itemSku']
    itemNamePOST = request.POST['itemName']
    itemAislePOST = request.POST['itemAisle']
    if itemSkuPOST != '':
        context = InventoryModel.objects.filter(itemSKU=itemSkuPOST)
        return render(request, "home.html", {'query': context})
    if itemNamePOST != '':
        context = InventoryModel.objects.filter(itemName=itemNamePOST)
        return render(request, "home.html", {'query': context})
    if itemAislePOST != '':
        context = InventoryModel.objects.filter(itemAisle=itemAislePOST)
        return render(request, "home.html", {'query': context})
