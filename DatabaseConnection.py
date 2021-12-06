import mysql.connector
class DatabaseConnection:
        mydb=mysql.connector.connect(host="localhost",user="root",password="Happy420@",port="3306",database="Pythonsqltask")
        mycursor=mydb.cursor()
        if mycursor:
            print("Connected Sucessfully!")
        else:
            print("Connection Failed!")