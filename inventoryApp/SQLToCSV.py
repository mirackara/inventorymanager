import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str

# Convert rows from database to csv file
def convertData(context,path):
    fields = ['itemSKU', 'itemName', 'itemAmount', 'itemAisle']
    csvList = []
    for item in context:
        rowToAdd = [item.itemSKU, item.itemName, item.itemAmount, item.itemAisle]
        csvList.append(rowToAdd)
    with open(path, 'w+', newline='') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(csvList)
    f.close()
    fileToDownload = open(path)
    response = HttpResponse(fileToDownload, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('inventoryCSV.csv')
    print("Download Sent!")
    return response
