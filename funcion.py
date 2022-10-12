import mysql.connector
#establishing the connection
import sys
sys.path.append("index")
import index as i
print(i.elements)

conn = mysql.connector.connect(
   user='root', password='', host='127.0.0.1', database='twitter'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
# Preparing SQL query to INSERT a record into the database.
sql= "insert into dato(twitter) values('user')"
#values=("elements")
try:
   # Executing the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   conn.commit()
except:
   # Rolling back in case of error
   conn.rollback()
# Closing the connection
conn.close()