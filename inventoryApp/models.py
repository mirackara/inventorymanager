from django.db import models

class InventoryModel(models.Model):
    # fields of the model
    itemSKU = models.CharField(max_length=200)
    itemName = models.CharField(max_length=200)
    itemAmount = models.IntegerField()
    itemAisle = models.CharField(max_length=201)

