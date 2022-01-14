import os
from django.shortcuts import render, redirect
from .models import InventoryModel
from .SQLToCSV import convertData
from .addToSQL import addToSQL
from .form import InventoryForm
from .searchSQL import searchSQL

# Delete Existing Item
def deleteHandler(request, itemSKU):
    InventoryModel.objects.filter(itemSKU=itemSKU).delete()
    return redirect('/')


# Edit Existing Item
def editHandler(request, itemSKU):
    if 'update' in request.POST:
        # Retrieve Item from DB
        model = InventoryModel.objects.get(itemSKU=itemSKU)
        # Change values
        print(request.POST)
        model.itemName = request.POST['itemName']
        model.itemSKU = itemSKU
        model.itemAmount = request.POST['itemAmount']
        model.itemAisle = request.POST['itemAisle']

        model.save()
        return redirect('/')
    # Show Editing Page
    else:
        item = InventoryModel.objects.get(itemSKU=itemSKU)
        form = InventoryForm(instance=item)
        return render(request, "updateItem.html", {'form': form})

def showItemList(request):
    context = InventoryModel.objects.all()
    return render(request, "home.html", {'query': context})
# Add Item to DB
def addHandler(request):
    # Initial Load
    if request.POST == {}:
        return render(request, "addItem.html")
    print(request.POST)
    if 'cancelAdd' in request.POST:
        return redirect('/')
    if 'itemSku' in request.POST and 'itemName' in request.POST \
            and 'itemAmount' in request.POST and 'itemAisle' in request.POST:
        addToSQL(request)
        return redirect('/')


def indexHandler(request, showList=False):
    # Initial Load
    if request.POST == {}:
        context = InventoryModel.objects.all()
        return render(request, "home.html", {'query': context})
    # Add to Database Button
    if 'addToDB' in request.POST:
        return redirect('/add/')
    if 'listInventory' in request.POST or showList:
        return showItemList(request)
    # Search for Row Button
    if 'searchDB' in request.POST:
        return searchSQL(request)
        # Convert to CSV Button
    if 'convertToCSV' in request.POST:
        csvDir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        filePath = os.path.join(csvDir, 'inventoryCSV.csv')
        context = InventoryModel.objects.all()
        return convertData(context, filePath)
    return render(request, "home.html")
