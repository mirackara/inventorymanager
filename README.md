# inventory manager

<h2>Description</h2>
• This is an inventory manager that shows current inventory levels and allows searching of all inventory or aisle. 
<h2> How To Use </h2>
You must have Python 3 installed. The project was tested and developed using Python 3.8.

Download the desired release's source code on GitHub (NOTE: The project is currently configured to use sqlite3 instead of MySQL, however MySQL is recommended if multiple users are using the program). 

First, make sure the dependancies are downloaded and installed. You can do this easily with the following command:
```shell
$  pip install -r requirements.txt
```

Navigate to the project directory, start the script with the following command:

```shell
$  python manage.py runserver 
```
This will start the web application on a locally hosted server.

<h2>Requirements</h2>

asgiref==3.4.1

backports.zoneinfo==0.2.1

Django==4.0.1

mysqlclient==2.1.0

sqlparse==0.4.2
