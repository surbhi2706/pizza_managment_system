def updateProfile(conn,uname):
    cursor = conn.cursor()
    print("1)FirstName        2)LastName        3)PhoneNumber        4)Gender")
    print("5)DateOfBirth      6)Age             7)Email              8)Address")
    ch = input("Enter your choice: ")
    print()
    if ch=='1':
        fname = input("Enter new FirstName: ")
        cursor.execute("update user_view set First_Name='%s' where User_Name='%s'"%(fname,uname))
        conn.commit()
        print("\nFirstName Updated in {} Profile\n".format(uname))
    elif ch=='2':
        lname = input("Enter new LastName: ")
        cursor.execute("update user_view set Last_Name='%s' where User_Name='%s'" % (lname, uname))
        conn.commit()
        print("\nLastName Updated in {} Profile\n".format(uname))
    elif ch=='3':
        phno = int(input("Enter new PhoneNumber: "))
        cursor.execute("update user_view set PHNO='%d' where User_Name='%s'"%(phno,uname))
        conn.commit()
        print("\nPhoneNumber Updated in {} Profile\n".format(uname))
    elif ch=='4':
        gen = input("Enter new Gender: ")
        cursor.execute("update user_view set Gender='%s' where User_Name='%s'"%(gen,uname))
        conn.commit()
        print("\nGender Updated in {} Profile\n".format(uname))
    elif ch=='5':
        dob = input("Enter new DateOfBirth(YYYY-MM-DD): ")
        cursor.execute("update user_view set DOB='%s' where User_Name='%s'"%(dob,uname))
        conn.commit()
        print("\nDateOfBirth Updated in {} Profile\n".format(uname))
    elif ch == '6':
        age = int(input("Enter new Age: "))
        cursor.execute("update user_view set Age='%d' where User_Name='%s'" % (age, uname))
        conn.commit()
        print("\nAge Updated in {} Profile\n".format(uname))
    elif ch == '7':
        email = input("Enter new Email: ")
        cursor.execute("update user_view set Email='%s' where User_Name='%s'" % (email, uname))
        conn.commit()
        print("\nEmail Updated in {} Profile\n".format(uname))
    elif ch == '8':
        addr = input("Enter new Address: ")
        cursor.execute("update user_view set Address='%s' where User_Name='%s'" % (addr, uname))
        conn.commit()
        print("\nAddress Updated in {} Profile\n".format(uname))
    else:
        print("\nProfile not Updated due to invalid choice\n")

def viewProfile(cursor,uname):
    print("***** Profile Details of {} *****".format(uname))
    cursor.execute("select * from user_view where User_Name='%s'"%(uname))
    row = cursor.fetchone()
    print("\tFullName: \t\t\t{} {}\n\tUserName: \t\t\t{}\n\tPHNO: \t\t\t\t{}\n\tGender: \t\t\t{}".format(row[0],row[1],row[2],row[3],row[4]))
    print("\tDateOfBirth: \t\t\t{}\n\tAge: \t\t\t\t{}\n\tEmail: \t\t\t\t{}\n\tAddress: \t\t\t{}\n".format(row[5],row[6],row[7],row[8]))

def delProfile(cursor,uname):
    cursor.execute("delete from user where User_Name = '%s'"%(uname))

def placeOrders(cursor,uname):
    data1 = ("Veg","Non-Veg")
    data2 = ("Pizza","Sides","Drinks","Desserts")
    typ = int(input("Which type do you prefer[  1)Veg  2)Non-Veg  3)Both ][valid for the whole order]: "))
    if typ not in [1,2,3]:
        raise ValueError("Enter valid type[ Please select 1 for Veg, 2 for Non-Veg, 3 for Both(Veg and Non-Veg) ]")
    flag=1
    order = []
    s1 = "select ItemID,Item_Name,Type,Price from items where Type='%s' and Category='%s'"
    if typ == 3:
        s1 = "select ItemID,Item_Name,Type,Price from items where Category='%s'"
    while flag:
        cat = int(input("Which category would you like to have[  1)Pizza  2)Sides  3)Drinks  4)Desserts ]: "))
        if cat not in [1,2,3,4]:
            print("\nPlease enter Valid Category\n")
            return
        if typ == 3:
            cursor.execute(s1 % (data2[cat - 1]))
        else:
            cursor.execute(s1%(data1[typ-1],data2[cat-1]))
        rows = cursor.fetchall()
        print("\n***** Here are our {} *****".format(data2[cat - 1]))
        print(" {:<19} {:<30} {:<15} {:<20}".format("ItemID", "ItemName", "Type", "Price"))
        print("{:<19} {:<30} {:<15} {:<20}".format("--------", "----------------------", "----------", "-------"))
        for row in rows:
            print(" {:<19} {:<30} {:<15} {:<20}".format(row[0],row[1],row[2],row[3]))
        print()
        n = int(input("Enter no. of items you want from above list: "))
        item=[]
        for i in range(n):
            print("\nItem {}:".format(i+1))
            iid = int(input("Enter ItemID: "))
            iqt = int(input("Enter Quantity: "))
            item.append((iid,iqt))
        order.extend(item)
        print()
        ch = input("Do you want to add more items(y/n): ")
        print()
        if ch == 'n':
            flag=0
    deliv = input("Select the mode[  1)Delivered at your Address    2)Takeaway from the Store ]: ")
    dist=0
    fare=0
    while deliv == '1':
        x = float(input("Enter your distance(KM)[>0.0]: "))
        if x<=0:
            print("Please enter valid distance\n")
            continue
        dist += x

        print()
        break
    if dist>=1 and dist<3 :
        fare = 30
    elif dist>=3 and dist<5 :
        fare = 40
    elif dist>=5 and dist<10:
        fare = 60
    elif dist>=10:
        fare = dist*10
    s2 = "insert into orders (Order_ID,User_ID,CreatedOn,Item_Name,Quantity,Amount,Total_Amount,Order_Status,Item_Type,Item_Category) values ('%s','%s','%s','%s','%d','%.2f','%.2f','%s','%s','%s')"
    cursor.execute("select Order_ID from orders order by Order_ID desc limit 1")
    x = cursor.fetchone()
    oid = 'ORD101'
    if x is not None:
        oid = 'ORD' + str(int(x[0][3:]) + 1)
    fprice = 0
    cursor.execute("select User_ID from user where User_Name='%s'" % (uname))
    uid = cursor.fetchone()[0]
    cursor.execute("select now()")
    cdate = cursor.fetchone()[0]
    ostat = "Active"
    tqty=0
    itype=""
    for itm in order:
        cursor.execute("select * from items where ItemID='%d'"%(itm[0]))
        idata = cursor.fetchone()
        iname,itype,icat,iprice,iqty = idata[1],idata[2],idata[3],idata[4],itm[1]
        tprice = iprice * iqty
        fprice += tprice
        tqty += iqty
        cursor.execute(s2%(oid,uid,cdate,iname,iqty,iprice,tprice,ostat,itype,icat))
    if typ == 3:
        itype="Both"
    s3 = "insert into orders (Order_ID,User_ID,Item_Type,Item_Name,CreatedOn,Quantity,Tax,Delivery_Charge,Discount,Amount,Total_Amount,Order_Status) values ('%s','%s','%s','Final Billing Row','%s','%d','%.2f','%.2f','%.2f','%.2f','%.2f','%s')"
    disc=0
    iprice=fprice
    if fprice>=500 and fprice<1000:
        disc += 0.05*fprice
    elif fprice>=1000 and fprice<1500:
        disc += 0.1*fprice
    elif fprice>=1500:
        disc += 0.15*fprice
    fprice-=disc
    tx = 0.05*fprice
    fprice += tx
    fprice += fare
    cursor.execute(s3%(oid,uid,itype,cdate,tqty,tx,fare,disc,iprice,fprice,ostat))

def viewOrders(cursor,uname):
    s = "select * from orders where User_ID=(select User_ID from user where User_Name='%s') order by Order_ID"
    cursor.execute(s%(uname))
    rows = cursor.fetchall()
    if rows == []:
        print("No Orders placed by {} till now\n".format(uname))
        return
    print("***** Order Details of {} *****".format(uname))
    print("{:<10} {:<15} {:<30} {:<30} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15} {:<25} {:<20} {:<20}".format(" SNo","OrderID","CreatedOn","ItemName","ItemType","ItemCategory","Quantity","Amount","Discount","Tax","DeliveryCharges","TotalAmount","OrderStatus",))
    print("{:<9} {:<15} {:<30} {:<30} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15} {:<25} {:<20} {:<20}".format("-----","---------","---------------------","----------------------","----------","--------------","----------","--------","----------","-----","-----------------","-------------","-------------",))
    for row in rows:
        print(" {:<9} {:<15} {:<30} {:<30} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15} {:<25} {:<20} {:<20}".format(row[0],row[1],str(row[3]),row[4],row[12],str(row[13]),row[5],row[6],str(row[9]),str(row[7]),str(row[8]),row[10],row[11],))
        if row[4] == "Final Billing Row":
            print()
    print()

def viewOrderByID(cursor,oid):
    cursor.execute("select * from orders where Order_ID='%s'" % oid)
    rows = cursor.fetchall()
    print("\nDetails of OrderID %s you want to cancel" % oid)
    print("{:<10} {:<15} {:<30} {:<30} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15} {:<25} {:<20} {:<20}".format(" SNo","OrderID","CreatedOn","ItemName","ItemType","ItemCategory","Quantity","Amount","Discount","Tax","DeliveryCharges","TotalAmount","OrderStatus",))
    print("{:<9} {:<15} {:<30} {:<30} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15} {:<25} {:<20} {:<20}".format("-----","---------","---------------------","----------------------","----------","--------------","----------","--------","----------","-----","-----------------","-------------","-------------",))
    for row in rows:
        print(" {:<9} {:<15} {:<30} {:<30} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15} {:<25} {:<20} {:<20}".format(row[0],row[1],str(row[3]),row[4],row[12],str(row[13]),row[5],row[6],str(row[9]),str(row[7]),str(row[8]),row[10],row[11],))
    print()
    ch = input("Are you sure to cancel above order(y/n): ")
    if ch == 'y':
        return 1
    return 0

def cancelOrders(conn,uname):
    cursor = conn.cursor()
    cursor.execute("select distinct(Order_ID) from orders where User_ID=(select User_ID from user where User_Name='%s') and Order_Status='Active'"%(uname))
    rows = cursor.fetchall()
    if rows==[]:
        print("No active order exists for {}\n".format(uname))
        return
    lst=[]
    for row in rows:
        lst.append(row[0])
    print("Active OrderIDs: {}".format(lst))
    ch = int(input("Enter position of OrderID from above list(Enter >0): "))
    if ch == 0:
        raise IndexError()
    x = viewOrderByID(cursor,rows[ch-1])
    if x == 0:
        print("\nOrder %s is not Cancelled !!!\n" % rows[ch-1])
        return
    cursor.execute("update orders set Order_Status='Cancelled' where Order_ID='%s'" % rows[ch-1])
    print("\nOrder %s is Cancelled successfully !!!\n" % rows[ch-1])
    conn.commit()

def home(conn,uname):
    cursor = conn.cursor()
    flag = 1
    while flag:
        try:
            print("1) Update Profile Details        2) View Profile Details        3) Delete your Account        4) Log Out")
            print("5) Place an Order                6) View your Orders            7) Cancel your Order")
            ch = input("Enter your choice: ")
            print()
            if ch == '1':
                try:
                    updateProfile(conn,uname)
                except sqlconn.DatabaseError as err:
                    print("\nError: {}\n".format(err))
                except ValueError as err:
                    print("\nError: {}\nPlease enter valid data\n".format(err))
            elif ch == '2':
                viewProfile(cursor,uname)
            elif ch == '3':
                delProfile(cursor,uname)
                conn.commit()
                print(uname,"Account Deleted\n")
                flag=0
            elif ch == '4':
                print("Logged Out from {}\n".format(uname))
                flag=0
            elif ch == '5':
                placeOrders(cursor,uname)
                conn.commit()
            elif ch == '6':
                viewOrders(cursor,uname)
            elif ch == '7':
                try:
                    cancelOrders(conn,uname)
                except IndexError:
                    print("\nError: Please enter valid Position\n")
            else:
                print("Please enter valid choice\n")
        except ValueError as err:
            print("\nError: {}\n".format(err))

def register(cursor):
    print()
    cursor.execute("select * from user order by User_ID desc limit 1")
    id = cursor.fetchone()
    newid = "U101"
    if id is not None:
        newid = 'U'+str(int(id[0][1:])+1)
    try:
        newfname = input("Enter your First Name: ")
        newlname = input("Enter your Last Name: ")
        newuname = input("Enter your User Name: ")
        newpass = input("Enter your Password: ")
        newphno = int(input("Enter Phone Number(10 digits): "))
        x = input("Enter you Gender(m/f): ")
        newgen=""
        if x == 'm':
            newgen = "Male"
        elif x == 'f':
            newgen = "Female"
        else:
            raise ValueError("Gender(Type either 'm' or 'f')")
        newdob = input("Enter your DateOfBirth(YYYY-MM-DD): ")
        newage = int(input("Enter your Age: "))
        newemail = input("Enter your Email: ")
        newaddr = input("Enter your Address: ")
        tup = (newid,newfname,newlname,newuname,newpass,newphno,newgen,newdob,newage,newemail,newaddr)
        cursor.execute("insert into user values('%s','%s','%s','%s','%s','%d','%s','%s','%d','%s','%s')"%tup)
        print("\nUser {} Registered Successfully !!!\n".format(newuname))
    except sqlconn.DatabaseError as err:
        print("\nError: {}\n".format(err))
    except ValueError as err:
        print("\nError: {}\nPlease enter valid data\n".format(err))

def login(conn):
    print()
    cursor = conn.cursor()
    uname = input("Enter your UserName: ")
    cursor.execute("select Password,First_Name,Last_Name from user where User_Name='%s'" % (uname))
    row = cursor.fetchone()
    if row == None:
        print("User does not exist (Can register as a new user / Login with correct username)\n")
        return
    opwd,ofname,olname = row
    npwd = input("Enter your Password: ")
    if opwd != npwd:
        print("Incorrect Password\n")
        return
    print("\nLogin Successful !!!  Hi {} {}\n".format(ofname,olname))
    home(conn,uname)

def start(conn):
    cursor = conn.cursor()
    print("************************************** Welcome to Pizza Hut **************************************")
    flag = 1
    while flag:
        print("1) Register as new user                         2) Login as a user                         3) Exit")
        ch = input("Enter your choice: ")
        if(ch=='1'):
            register(cursor)
            conn.commit()
        elif(ch=='2'):
            login(conn)
        elif(ch=='3'):
            flag=0
        else:
            print("Enter valid choice\n")
    print("\n                                       Hope you enjoyed !!!")
    print("                                          😃 Thank You 😃")

import mysql.connector as sqlconn
conn = sqlconn.connect(host='localhost', database='Surbhi_PizzaManagement', user='root', password='surbhi')
if conn.is_connected():
    print("Connected")
start(conn)