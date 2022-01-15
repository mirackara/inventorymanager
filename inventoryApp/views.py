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

# Display table
def showItemList(request):
    context = InventoryModel.objects.all()
    return render(request, "home.html", {'query': context})


# Add Item to DB
def addHandler(request):
    # Initial Load
    if request.POST == {}:
        return render(request, "addItem.html")
    if 'cancelAdd' in request.POST:
        return redirect('/')
    if 'keepFirst' in request.POST:
        return redirect('/')
    if 'keepSecond' in request.POST:
        InventoryModel.objects.filter(itemSKU=request.POST['itemTwoSKU']).delete()
        post = request.POST.copy()  # to make it mutable
        post['itemSku'] = post['itemTwoSKU']
        post['itemName'] = post['itemTwoName']
        post['itemAmount'] = post['itemTwoAmount']
        post['itemAisle'] = post['itemTwoAisle']
        request.POST = post
        return redirect('/')
    # If item was successfully added
    if addToSQL(request):
        return redirect('/')
    else:
        attemptedAdd = [request.POST['itemSku'],request.POST['itemName'],request.POST['itemAmount'],request.POST['itemAisle']]
        item = InventoryModel.objects.get(itemSKU=request.POST['itemSku'])
        form = [[item.itemSKU,item.itemName,item.itemAisle,item.itemAmount], attemptedAdd]
        return render(request, "updateItem.html", {'form': form})

def indexHandler(request, showList=False):
    # Initial Load
    if request.POST == {}:
        context = InventoryModel.objects.all()
        return render(request, "home.html", {'query': context})
    # Add to Database
    if 'addToDB' in request.POST:
        return redirect('/add/')
    # Show List
    if 'listInventory' in request.POST or showList:
        return showItemList(request)
    # Search for Row
    if 'searchDB' in request.POST:
        return searchSQL(request)
    # Convert to CSV
    if 'convertToCSV' in request.POST:
        # Get path of inventoryCSV.csv file
        csvDir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        filePath = os.path.join(csvDir, 'inventoryCSV.csv')
        context = InventoryModel.objects.all()
        return convertData(context, filePath)
    return render(request, "home.html")
