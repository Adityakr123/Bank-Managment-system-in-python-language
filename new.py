import mysql.connector
import os
from time import sleep
import getpass
import random
from datetime import datetime


class accholder_details:
    name = ''
    address = ''
    userid = ''
    password = ''
    confirmpassword = ''
    dob = ''
    adharcardno = ''
    tp = ''
    confirmtp = ''
    phonenum = ''
    emailid = ''
    pannumber = ''
    initialammount = ''
    accnumber = ''
    initialdate = ''
ob1 = accholder_details()



def signin():

    m = input("Enter Your name:")
    ob1.name+= m
    m = input("Enter your address:")
    ob1.address += m
    while (ob1.confirmpassword!= ob1.password):
        n = input("Enter your Confirmation Password:")
        ob1.confirmpassword+= n
    m = input("Enter your date of birth:")
    ob1.dob += m
    m = input("Enter your aadhar card no:")
    ob1.adharcardno += m
    print("\n")
    print("\033[1;31;43m If you want to see the password press 1 otherwise press 0.\n")
    ob1.seepass = int(input())
    if ob1.seepass == 1:
        ob1.password = input("enter ur password:")
    elif ob1.seepass== 0:
        ob1.password = getpass.getpass(prompt='Password:') 
    print("\nIf you want to see the Confirmed password press 1 otherwise press 0.\n")
    ob1.cseepass = int(input())
    if ob1.cseepass == 1:
        ob1.confirmpassword = input("enter ur confirmed password:")
    elif ob1.cseepass == 0:
        ob1.confirmpassword = getpass.getpass(prompt='Confirm Password:')
    while (ob1.password != ob1.confirmpassword):
        ob1.confirmpassword = (input("confirm ur password:"))

    print("\nIf you want to see your transection password press 1 otherwise press 0.\n")
    ob1.tpseepass = int(input())
    if ob1.tpseepass == 1:
        ob1.tp = input("enter ur Transection password:")
    elif ob1.tpseepass==0:
        ob1.tp = getpass.getpass(prompt='Transection Password:')
    print("\nIf you want to see the Confrimed trensction  password while writing press 1 otherwise press 0.\n")
    ob1.ctpseepass = int(input())
    if ob1.ctpseepass == 1:
        ob1.confirmtp = input("enter ur password:")
    elif ob1.ctpseepass == 0:
        ob1.confirmtp = getpass.getpass(prompt='Transection Password:')
    while (ob1.tp != ob1.confirmtp):
        ob1.confirmtp = input("confirm ur transaction password:")
    m = input("Enter your Phone number:")
    ob1.phonenum += m
    m = input("Enter your Email ID:")
    ob1.emailid +=m
    m = input("Enter your Pan Number:")
    ob1.pannumber+=m
    m = input("Enter your Initial Amount:")
    ob1.initialammount+= m

    m = input("Enter your Today's Date :")
    ob1.initialdate+=m

    screen_clear()

    ob1.accnumber = ob1.adharcardno[0:6] + ob1.phonenum[4:9]
    print('\n Your account number is:' + ob1.accnumber)


    ob1.userid = ob1.name + '@' + ob1.phonenum[5:9]
    print("\nYour USER-ID is:" + ob1.userid)


    print("\n")
    print("\033[1;32;43m which type of account you want to make \n press 1 for saving \n press 2 for current\n")
    typeacc=int(input())
    if typeacc==1:
        savingintrest()
    elif typeacc==2:
        currentintrest()
    mydb = mysql.connector.connect(host="localhost",user = "root",passwd = "ghtthht9321",database = "abc")
    mycursor= mydb.cursor()

    sql = "INSERT INTO credential1(name ,dob , adharcardno , pasword , tp , phonenum , emailid , pannumber ,address,initialammount ,accnumber ,userid,initaldate)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (ob1.name, ob1.dob, ob1.adharcardno, ob1.password, ob1.tp, ob1.phonenum, ob1.emailid, ob1.pannumber,ob1.address, ob1.initialammount, ob1.accnumber, ob1.userid,ob1.initialdate)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.execute("select * from credential1")
    for i in mycursor:
        print(i)
    start()


def loginmenu():
    aydb = mysql.connector.connect(host='localhost',user='root', password = "ghtthht9321",db='abc')
    print("\n")
    print("\033[1;31;43m \n")
    
    

    print("1. Press 1 for change addres \n2. Press 2 for money deposite\n3. Press 3 for bank withdraw \n4. Press 4 for print bank statement \n5. Press 5 transfer money \n6. Press 6 to close account \n7. Press 7 to change Phone Number\n8. Press 8 to change the Email-ID\n9. Press 9 to change the password\n10. Press 10 to Change transection password\n11. Press 11 to logout.")
    n=int(input())
    if n==1:
        corsor = aydb.cursor()
        a=input("enter your new address ")  
        b=input("enter your account no ")  
        sql = "UPDATE credential1 SET address=%s  WHERE accnumber= %s"
        val=(a,b)
        corsor.execute(sql,val)
        aydb.commit()
        corsor.execute("select * from credential1")
        print("\naddress sucessfully changed\n")
        a= int(input("to do back to main menu press 1 or to exit press 0:"))
        while(a!=1 and a!=0):
            a = int(input("Please Enter the Correct Number:"))
        if a == 1:
            loginmenu()
        elif a == 0:
            exit()
        else:
            pass    
        mydb.close()

    elif n==2:
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        adiydb = mysql.connector.connect(host='localhost',user='root', password = "ghtthht9321",db='abc')
        adicorsor = adiydb.cursor()
        ammount=int(input("enter amount which you have to deposite "))
        accno=input("enter your account no ")    
        
        s=''
                 
        adicorsor.execute("select* from credential1")
        for i in adicorsor:
            print(i)
            if i[10] == accno:
                s+=i[9]
                print(s)
              
        z=int(s)
        z=z+ammount
        l=str(z)
        print(l)
        

        maydb = mysql.connector.connect(host='localhost',user='root', password = "ghtthht9321",db='abc') 
        corsur = maydb.cursor()
        ql = "UPDATE credential1 SET initialammount=%s WHERE accnumber= %s"

        al=(l,accno)
        corsur.execute(ql,al)
        maydb.commit()
        corsur.execute("select * from credential1")
        for i in corsur: 
            print(i)
        print("\nMoney deposited \n")
        wq=str(ammount)
        try:
            corsur.execute
            corsur.execute("CREATE TABLE statement ( balance varchar(20),deposit varchar(20),withdrawl varchar(20), accnumber varchar(20), date varchar(20))")
        except:
            print("table exisits")
        aql = "INSERT INTO statement(balance ,deposit,accnumber,date)VALUES(%s,%s,%s,%s)"
        aal = (s,wq,accno,date_time)
        corsur.execute(aql,aal)
        maydb.commit()   
        corsur.execute("select*from statement")
        a= int(input("to do back to main menu press 1 or to exit press 0:"))
        while(a!=1 and a!=0):
            a = int(input("Please Enter the Correct Number:"))
        if a == 1:
            loginmenu()
        elif a == 0:
            exit()
        else:
            pass
        
    elif n==3:
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        adiydb = mysql.connector.connect(host='localhost',user='root', password = "ghtthht9321",db='abc')
        adicorsor = adiydb.cursor()
        ammount=int(input("enter amount which you have to withdraw "))
        accno=input("enter your account no ")    
        
        s=''
                 
        adicorsor.execute("select* from credential1")
        for i in adicorsor:
            if i[10] == accno:
                s+=i[9]
                print(s)
              
        z=int(s)
        z=z-ammount
        l=str(z)

        tp = input("Enter you Tp:")
        
        wq= str(ammount)
        maydb = mysql.connector.connect(host='localhost',user='root', password = "ghtthht9321",db='abc') 
        corsor = maydb.cursor()
        ql = "UPDATE credential1 SET initialammount=%s WHERE accnumber= %s and tp = %s"

        al=(l,accno,tp)
        corsor.execute(ql,al)
        maydb.commit()
        corsor.execute("select * from credential1")
        for i in corsor: 
            print(i)
        try:
            corsor.execute
            corsor.execute("CREATE TABLE statement ( balance varchar(20),deposit varchar(20),withdrawl varchar(20), accnumber varchar(20), date varchar(20))")
        except:
            print("table exisits")
        aql = "INSERT INTO statement(balance ,withdrawl,accnumber,date)VALUES(%s,%s,%s,%s)"
        aal = (s,wq,accno,date_time)
        corsor.execute(aql,aal)
        maydb.commit()   
        corsor.execute("select*from credential1")
        print("\nMoney withdrawal \n")
        a= int(input("to do back to main menu press 1 or to exit press 0:"))
        while(a!=1 and a!=0):
            a = int(input("Please Enter the Correct Number:"))
        if a == 1:
            loginmenu()
        elif a == 0:
            exit()
        else:
            pass


    elif n==4:
        maydb = mysql.connector.connect(host='localhost',user='root', password = "ghtthht9321",db='abc') 
        corsur = maydb.cursor()
        a=input("enter account number of which you want to display statement:")
        print(" balance  deposit  withdraw   accnumber    date    time")
        corsur.execute("select*from statement")
        for i in corsur:
            if i[3]==a:
               print(i)
        

        a= int(input("to do back to main menu press 1 or to exit press 0:"))
        while(a!=1 and a!=0):
            a = int(input("Please Enter the Correct Number:"))
        if a == 1:
            loginmenu()
        elif a == 0:
            exit()
        else:
            pass
            

    elif n==5:
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        ammount=int(input("enter amount which you have to transfer "))
        accno=input("enter your account no ")
        maydb = mysql.connector.connect(host='localhost',user='root', password = "ghtthht9321",db='abc') 
        accno1=input("enter account number where you want to transfer money")
        sursor=maydb.cursor()
        sursor.execute("select*from credential1")
        for k in sursor:
            print(k)
            if k[10]==accno1:
                print(k)
                s=''
                adiydb = mysql.connector.connect(host='localhost',user='root', password = "ghtthht9321",db='abc')
                adicorsor = adiydb.cursor()         
                adicorsor.execute("select* from credential1")
                for i in adicorsor:
                    print(i)
                    if i[10] == accno:
                        s+=i[9]
                        print(s)
                      
                z=int(s)
                z=z-ammount
                l=str(z)
                tp = input("Enter you Transection Password:")
                
                ql = "UPDATE credential1 SET initialammount=%s WHERE accnumber= %s and tp = %s"

                al=(l,accno,tp)
                adicorsor.execute(ql,al)
                adiydb.commit()
                u=''
                adicorsor.execute("select  * from credential1")
                for i in adicorsor:
                    print(i)
                    if i[10] == accno1:
                        u+=i[9]
                        print(u)
                      
                q=int(u)
                q=q+ammount
                x=str(q)
                

                maydb = mysql.connector.connect(host='localhost',user='root', password = "ghtthht9321",db='abc') 
                corsur = maydb.cursor()
                ql = "UPDATE credential1 SET initialammount=%s WHERE accnumber= %s"

                al=(q,accno1)
                corsur.execute(ql,al)
                maydb.commit()
                corsur.execute("select * from credential1")
                for i in corsur: 
                    print(i)
                print("\nMoney deposited \n")
                a= int(input("to do back to main menu press 1 or to exit press 0:"))
        while(a!=1 and a!=0):
            a = int(input("Please Enter the Correct Number:"))
        if a == 1:
            start()
        elif a == 0:
            exit()
        else:
            pass

        maydb.close()    
            
            
        



    elif n==6:

        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        aydb = mysql.connector.connect(host='localhost', database='abc', user='root', password='ghtthht9321')
        corsor = aydb.cursor()
        acno = input('Enter customer Account No :')
        sql ='update credential1 set accnumber="close" where accnumber ='+acno+';'
        
        corsor.execute(sql)
        aydb.commit()
        print('Account closed')
        print("\naccount deleted sucessfully \n")
        try:
            corsor.execute
            corsor.execute("CREATE TABLE closed_account ( accnumber varchar(20),date varchar(20))")
        except:
            print("table exisits")
        aql = "INSERT INTO closed_account(accnumber,date)VALUES(%s,%s)"
        aal = (acno,date_time)
        corsor.execute(aql,aal)
        aydb.commit()

        
        a= int(input("to do back to main menu press 1 or to exit press 0:"))
        while(a!=1 and a!=0):
            a = int(input("Please Enter the Correct Number:"))
        if a == 1:
            loginmenu()
        elif a == 0:
            exit()
        else:
            pass

        aydb.close()
    elif n==7:
        corsor = aydb.cursor()
        a=input("enter your new phone no: ")  
        b=input("enter your account password: ")  
        sql = "UPDATE credential1 SET phonenum=%s  WHERE pasword= %s"
        val=(a,b)
        corsor.execute(sql,val)
        aydb.commit()
        corsor.execute("select * from credential1")
        print("\nphone number sucessfully changed\n")
        a= int(input("to do back to main menu press 1 or to exit press 0:"))
        while(a!=1 and a!=0):
            a = int(input("Please Enter the Correct Number:"))
        if a == 1:
            loginmenu()
        elif a == 0:
            exit()
        else:
            pass    


    
        aydb.close()

    elif n==8:
        corsor = aydb.cursor()
        a=input("enter your new email  ")  
        b=input("enter your account password ")  
        sql = "UPDATE credential1 SET emailid=%s  WHERE pasword= %s"
        val=(a,b)
        corsor.execute(sql,val)
        aydb.commit()
        corsor.execute("select * from credential1")
        print("\nemail  sucessfully changed\n")
        loginmenu()    


    
        aydb.close()
    elif n==9:
        corsor = aydb.cursor()
        a=input("enter your new password: ")  
        b=input("enter your account no:")  
        sql = "UPDATE credential1 SET pasword=%s  WHERE accnumber= %s"
        val=(a,b)
        corsor.execute(sql,val)
        aydb.commit()
        corsor.execute("select * from credential1")
        print("\npassword sucessfully changed\n")
        a= int(input("to do back to main menu press 1 or to exit press 0:"))
        while(a!=1 and a!=0):
            a = int(input("Please Enter the Correct Number:"))
        if a == 1:
            loginmenu()
        elif a == 0:
            exit()
        else:
            pass    


    
        aydb.close()

    elif n==10:
        corsor = aydb.cursor()
        a=input("enter your new Transection password:")  
        b=input("enter your account password:")  
        sql = "UPDATE credential1 SET tp=%s  WHERE pasword= %s"
        val=(a,b)
        corsor.execute(sql,val)
        aydb.commit()
        corsor.execute("select * from credential1")
        print("\nTransection password sucessfully changed\n")
        a= int(input("to do back to main menu press 1 or to exit press 0:"))
        while(a!=1 and a!=0):
            a = int(input("Please Enter the Correct Number:"))
        if a == 1:
            loginmenu()
        elif a == 0:
            exit()
        else:
            pass    


    
        aydb.close()

    elif n == 11:
        import time
        print("you are loggin out.")
        time.sleep(1.0)
        print('You have been logged out successfully !!')
        exit()




def capcha():   
    x=random.randint(1,1000)
    y=random.randint(1,1000)
    x=x*y
    i=0
    a=''
    while(x>1):
        m=int(x%10)
        
        if i%3==0:
            a+=chr(m+49)
            

        if i%2==0:
            a+=chr(m+97)
            
        else:
            a+=chr(m+65)
            
        x=x/10
        i=i+1
    print(a)

    
    print("\033[1;32;43m if you want to reload the capcha press 1 else 0\n")
    n=int(input())
    if n==1:
        capcha()
    else:
        b=input("enter above capcha\n")  
        if b==a:
            print("correct")
            loginmenu()
        else:
            capcha()

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="ghtthht9321",
    database="abc"
)
def savingintrest():
    print("\n THE INTREST GIVEN ON MONEY IS 7.5% IN OUR BANK ON SAVING ACCOUNT \n")
def currentintrest():
    print("\n THE INTREST GIVEN ON MONEY IS 0% IN OUR BANK ON SAVING ACCOUNT \n")

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


def admin():
    screen_clear()
    print("\033[1;33;42m \n")

    aydb = mysql.connector.connect(host='localhost', database='abc', user='root', password='ghtthht9321')
    corsor = aydb.cursor()

    print("WELCOME TO ADMIN ACCOUNT\n")
    username = input("ENTER USER NAME TO VALIDATE")
    i = 0
    while(username!="pythonproject"):
        if i <= 1:
            username = input("\nYOU ENTERED WRONG USER NAME \n ENTER USER NAME TO VALIDATE")
            i+=1
        else:
            admin()
        

    password=input("ENTER YOUR PASSWORD\n")
    k = 0
    while(password!="500083205@b31"):
        if k <= 1:
            password = input("\n YOU ENTERED WRONG PASSWORD\nENTER YOUR PASSWORD\n")
            k += 1
        else:
            admin()
    print("WELCOME MR ADMIN\n")
    print("Account      Date        Time")
    corsor.execute("select * from closed_account")
    for j in corsor:
        print(j)
    aydb.close()





def login():

    mycursor = mydb.cursor()
    print("\033[1;33;42m \n")

    checkuserid = input("Enter user id\n")
    checkpassword= input("Enter password\n")

    sql = "SELECT * FROM credential1"
    mycursor.execute(sql)
    for i in mycursor:
        if i[11] == checkuserid:
            ydb = mysql.connector.connect(
            host='localhost',
            user='root', 
            password = "ghtthht9321",
            db='abc',
            )
            cursor = ydb.cursor()
            ql = "SELECT * FROM credential1"
            cursor.execute(ql)
            for j in cursor:
                if j[3]==checkpassword:
                    capcha()
                    break
                else:
                    pass
            break    



def start():
    print("\033[1;32;40m                      WELCOME TO CENTRAL BANK OF INDIA \n \n\n")
    print("\033[1;33;40m 1. SIGNIN               2. LOGIN          3. ADMIN         4.QUIT\n")
    choice=int(input())
    while(0>choice<5):
        print("You entered wrong choice\n")
        choice = int(input())
    
    if choice==1: 
        signin()
            
    elif choice==2:
        login()
    elif choice==3:
        admin()
    elif choice==4:
        exit()
    else:
        print("\033[1;43;42m please enter correct choice\n")

start()