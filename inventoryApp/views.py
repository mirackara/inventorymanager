from django.shortcuts import render
from .models import InventoryModel


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = InventoryModel(request.POST or None)
    context['form'] = form

    model = InventoryModel(itemSKU=request.POST['itemSku'], itemName=request.POST['itemName'], itemAmount = request.POST['itemAmount'], itemAisle = request.POST['itemAisle'])  # create new model instance
    model.save()  # seve to db
    return render(request, "home.html", context)

# Create your views here.
def indexHandler(request):
    if request.POST == {}:
        print(request.POST)
        return render(request, "home.html")
    print(request.POST)
    if 'addToDB' in request.POST:
        if 'itemSku' in request.POST and 'itemName' in request.POST \
                and 'itemAmount' in request.POST and 'itemAisle' in request.POST:
            return create_view(request)
    if 'listInventory' in request.POST:
        context = InventoryModel.objects.all()

        return render(request, "home.html", {'query' : context})

    return render(request, "home.html")
