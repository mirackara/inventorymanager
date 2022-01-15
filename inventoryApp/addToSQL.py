from .models import InventoryModel

def addToSQL(request):
    itemSkuPOST = request.POST['itemSku']
    itemNamePOST = request.POST['itemName']
    itemAislePOST = request.POST['itemAisle']
    itemAmountPOST = request.POST['itemAmount']
    # If the user did not fill out any forms
    if itemNamePOST == '' or itemSkuPOST == '' or itemAislePOST == '' or itemAmountPOST == '':
        return
    if InventoryModel.objects.filter(itemSKU=itemSkuPOST).exists():
        print("Already Exists!")
        return False
    else:
        # New Inventory Model Instance
        model = InventoryModel(itemSKU=request.POST['itemSku'], itemName=request.POST['itemName'],
                               itemAmount=request.POST['itemAmount'],
                               itemAisle=request.POST['itemAisle'])
        # Save Model to DB
        model.save()
        return True
