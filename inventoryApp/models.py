from django.db import models

# Basic Model for database containing SKU, Name, Amount, and Aisle
# If more rows are to be added/removed this is where the changes should occur first!

class InventoryModel(models.Model):
    itemSKU = models.CharField(max_length=200)
    itemName = models.CharField(max_length=200)
    itemAmount = models.IntegerField()
    itemAisle = models.CharField(max_length=201)