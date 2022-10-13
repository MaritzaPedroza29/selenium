import mysql.connector


#establishing the connection
conexion = mysql.connector.connect(
   user='root', password='', host='127.0.0.1', database='twitter'
)

#Creating a cursor object using the cursor() method
cursor = conexion.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("SELECT DATABASE()")

#Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Connection established to: ",data)

#Closing the connection
conexion.close()