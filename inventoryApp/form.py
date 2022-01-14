from django import forms
from .models import InventoryModel

class InventoryForm(forms.ModelForm):
    class Meta:
        model = InventoryModel
        fields = ('itemSKU', 'itemName', 'itemAmount', 'itemAisle')
        labels = {
            'itemSKU': 'sku',
            'itemName': 'name',
            'itemAmount': 0,
            'itemAisle': 'A0'
        }
