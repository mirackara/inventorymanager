import mysql.connector

inventoryDB = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password"
)

inventoryCursor = inventoryDB.cursor()

inventoryCursor.execute("SHOW DATABASES")

for x in inventoryCursor:
  print(x)