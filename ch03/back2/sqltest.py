import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="123",
	database="test")

mycursor = mydb.cursor()

print(mycursor.execute("SHOW DATABASES"))