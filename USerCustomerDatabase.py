from DatabaseConnection import DatabaseConnection
def create_table_customers():

    DatabaseConnection.mycursor.execute("create table pythonsqltask.customersdetails(customerid int(20) primary key auto_increment,customername varchar(200),description varchar(200),location varchar(200))")
    DatabaseConnection.mydb.commit()
def create_table_users():

    DatabaseConnection.mycursor.execute("create table pythonsqltask.userdetails(userid int(20) primary key auto_increment,customerid int(20),FirstName varchar(200),LastName varchar(200),mobile varchar(200),email varchar(200))")
    DatabaseConnection.mydb.commit()

def insert_customer():
    sql_statement = "Insert Into pythonsqltask.customersdetails VALUES (%s,%s,%s,%s)"
    values = (int(input("Enter Your customerid ")),input("Enter Your customername "),input("Enter Your description "),input("Enter Your location "))
    DatabaseConnection.mycursor.execute(sql_statement, values)
    DatabaseConnection.mydb.commit()
    print("Detail Saved Successfully!")
def insert_users():
    sql_statement = "Insert Into pythonsqltask.userdetails VALUES (%s,%s,%s,%s,%s,%s)"
    values = (int(input("Enter Your userid ")),int(input("Enter Your customerid ")),input("Enter Your firstname "),input("Enter Your lastname "),input("Enter Your mobileno"),input("Enter Your email"))
    DatabaseConnection.mycursor.execute(sql_statement, values)
    DatabaseConnection.mydb.commit()
    print("Detail Saved Successfully!")
def Customer_name_id():
    DatabaseConnection.mycursor.execute("select customername,customerid from pythonsqltask.customersdetails")
    output = DatabaseConnection.mycursor.fetchall()
    for x in output:
        print(x)
def user_attached_user():
    DatabaseConnection.mycursor.execute("select count(userdetails.userid) from pythonsqltask.userdetails join pythonsqltask.customersdetails where userdetails.customerid=customersdetails.customerid")
    output = DatabaseConnection.mycursor.fetchall()
    for x in output:
        print(x)
def customer_noida():
    DatabaseConnection.mycursor.execute("SELECT * FROM  pythonsqltask.customersdetails where location='noida'")
    output = DatabaseConnection.mycursor.fetchall()
    for x in output:
        print(x)
def customer_NameWith_A():
    DatabaseConnection.mycursor.execute("select * from pythonsqltask.customersdetails where customerName like 'A%' ")
    output = DatabaseConnection.mycursor.fetchall()
    for x in output:
        print(x)
def User_sort():
    DatabaseConnection.mycursor.execute("select * from pythonsqltask.userdetails group by userid order by userid desc")
    output = DatabaseConnection.mycursor.fetchall()
    for x in output:
        print(x)
def Avg_user_count():
    DatabaseConnection.mycursor.execute("select avg(userdetails.userid) from pythonsqltask.userdetails join pythonsqltask.customersdetails where customersdetails.location='noida'")
    output = DatabaseConnection.mycursor.fetchall()
    for x in output:
        print(x)
def Total_User_Count():
    DatabaseConnection.mycursor.execute(" select count(userdetails.userid) from pythonsqltask.userdetails join pythonsqltask.customersdetails where customersdetails.customerid=userdetails.customerid and customersdetails.location='noida'")
    output = DatabaseConnection.mycursor.fetchall()
    for x in output:
        print(x)