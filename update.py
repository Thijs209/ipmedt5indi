import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "thijs",
    passwd = "",
    database = "communication"
)

mycursor = mydb.cursor()

mycursor.execute("UPDATE count SET amount = amount +1;")
mydb.commit()