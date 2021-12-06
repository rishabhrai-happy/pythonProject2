flag=True
while(flag):
    from USerCustomerDatabase import create_table_customers,create_table_users,insert_customer,insert_users,Customer_name_id,user_attached_user,customer_noida, \
        customer_NameWith_A,User_sort,Avg_user_count,Total_User_Count
    from DatabaseConnection import DatabaseConnection

    a = int(input("Enter Your Choice: "))
    if(a==1):
        create_table_customers()
        print("created table")
    if(a==2):
        create_table_users()
        print("usre trable created")
    if(a==3):
        insert_customer()
    if(a==4):
        insert_users()
    if(a==5):
        Customer_name_id()
    if(a==6):
        user_attached_user()
    if(a==7):
        customer_noida()
    if(a==8):
        customer_NameWith_A()
    if(a==9):
        User_sort()
    if(a==10):
        Avg_user_count()
    if(a==11):
        Total_User_Count()
    if(a==12):
        flag=False







