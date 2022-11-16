import mysql.connector
import credentials as cr

mydb = mysql.connector.connect(
  host=cr.host,
  user=cr.user,
  password=cr.password,
  database=cr.database
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM rawdata")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)