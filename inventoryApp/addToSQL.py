from .models import InventoryModel


def addToSQL(request):
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
