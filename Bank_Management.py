import math
import mysql.connector
from datetime import *
conn=mysql.connector.connect(user='root',host='localhost',password='vaibn')
cursor=conn.cursor()
data_saver=''
z=True
while z:
    s=(str)(input("DO YOU WANT TO DELETE PREVIOUS DATA OF RAJA BANK(YES OR NO):"))
    s=s.upper()
    if((s=="YES")or(s=="NO")):
        z=False
if(s=="YES"):
    cursor.execute('SHOW DATABASES')
    db=cursor.fetchall()
    print(db)
    c=0
    t1=('raja_bank',)
    for i in range(len(db)-1):
        if(db[i]==t1):
            cursor.execute("DROP DATABASE RAJA_BANK")
            c=1
    if(c==1):
        cursor.execute("CREATE DATABASE RAJA_BANK")
    else:
        cursor.execute("CREATE DATABASE RAJA_BANK")
d=0
if(s=="NO"):
    cursor.execute('SHOW DATABASES')
    db=cursor.fetchall()
    c=0
    t1=('raja_bank',)
    for i in db:
        if(i==t1):
           d=1
    if(d==1):
        pass
    else:
        cursor.execute("CREATE DATABASE RAJA_BANK")

cursor.execute("USE RAJA_BANK")
if(c==1):
    cursor.execute("""CREATE TABLE CREATE_BANK_ACCOUNT
                  (
                   AC_NAME VARCHAR(50) NOT NULL,
                   FA_HUS_NAME VARCHAR(50) NOT NULL,
                   M_NAME VARCHAR(50) NOT NULL,
                   D_O_B VARCHAR(11) NOT NULL,
                   NOMINEE_NAME VARCHAR(50) NOT NULL,
                   AADH_NO VARCHAR(50) NOT NULL UNIQUE,
                   ACC_PAN_NO VARCHAR(11) NOT NULL UNIQUE,
                   GUAR_PAN_NO VARCHAR(11) NOT NULL UNIQUE,
                   MOB_1 VARCHAR(50) NOT NULL UNIQUE,
                   MOB_2 VARCHAR(50),
                   PER_H_ADD VARCHAR(100) NOT NULL,
                   H_ADD VARCHAR(100) NOT NULL,
                   GARENTER_NAME VARCHAR(50) NOT NULL,
                   ACC_NO VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY
                   )""")
    cursor.execute("""CREATE TABLE CASH_DEPOSIT
                  (
                   ACC_NO VARCHAR(50) NOT NULL,
                   CASH_DEPOSITED VARCHAR(50) NOT NULL,
                   CURRENT_BALANCE VARCHAR(50),
                   PAN_CARD_NUMBER VARCHAR(50),
                   DATE VARCHAR(50),
                   TIME VARCHAR(10)
                   )""")
    cursor.execute("""CREATE TABLE CASH_WITHDRAWL
                  (
                   ACC_NO VARCHAR(50) NOT NULL,
                   CASH_WITHDRAWLED VARCHAR(50) NOT NULL,
                   CURRENT_BALANCE VARCHAR(50),
                   PAN_CARD_NUMBER VARCHAR(50),
                   DATE VARCHAR(50),
                   TIME VARCHAR(10)
                  )""")
    cursor.execute("""CREATE TABLE PASSBOOK
                  (
                   ACC_NO VARCHAR(50),
                   CASH_DEPOSITED VARCHAR(50),
                   CASH_WITHDRAWLED VARCHAR(50),
                   CURRENT_BALANCE VARCHAR(50),
                   PAN_CARD_NUMBER VARCHAR(50),
                   DATE VARCHAR(50),
                   TIME VARCHAR(10)
                   )""")
    
def main_menu():
   print("~"*134*2)
   print("CONNECTED TO RAJA BANK DATABASE.")
   print((" "*60),'WELCOME TO RAJA BANK')
   print((" "*60),"````````````````````")
   print("MAIN MENU:")
   print("1.CREATE BANK ACCOUNT")
   print("2.DEPOSIT CASH")
   print("3.CASH WITHDRAWL")
   print("4.PRINT PASSBOOK")
   print("5.TO EXIT BANK")
   ch=(str)(input("ENTER YOUR CHOICE:"))
   if(ch.isdigit()):
       ch=(int)(ch)
       pass
   else:
       main_menu()
   if(ch==1):
        print("~"*134*2)
        CR_BA_AC()#CREATE BANK ACCOUNT
   elif(ch==2):
        print("~"*134*2)
        DE_CA()#DEPOSIT CASH
   elif(ch==3):
        print("~"*134*2)
        CA_WI()#CASH WITHDRAWL
   elif(ch==4):
       print("~"*134*2)
       PR_PA()#PRINT PASSBOOK
   elif(ch==5):
       print("~"*134*2)
       exit()#TO EXIT 
   else:
       print("ENTERED CHOICE WAS INVALID.")
       print("PLEASE ENTER A VALID CHOICE.")
       print(("~")*268)
       print((" "*60),'WELCOME TO RAJA BANK')
       main_menu()
#_____________________________________________________________________________________________

def CR_BA_AC():
    first_name=(str)(input("ACCOUNT_HOLDER_FIRST_NAME:"))
    while(first_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        first_name=(str)(input("ACCOUNT_HOLDER_FIRST_NAME:"))
    last_name=(str)(input("ACCOUNT_HOLDER_LAST_NAME:"))
    while(last_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        last_name=(str)(input("ACCOUNT_HOLDER_LAST_NAME:"))
    acc_hol_name=first_name+" "+last_name#ACCOUNT HOLDER NAME
    first_name=(str)(input("FATHER'S/HUSBAND'S_FIRST_NAME:"))
    while(first_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        first_name=(str)(input("FATHER'S/HUSBAND'S_FIRST_NAME:"))
    last_name=(str)(input("FATHER'S/HUSBAND'S_LAST_NAME:"))
    while(last_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        last_name=(str)(input("FATHER'S/HUSBAND'S_LAST_NAME:"))
    father_husband_name=first_name+" "+last_name#ACCOUNT HOLDER'S FATHER NAME
    first_name=(str)(input("MOTHER'S_FIRST_NAME:"))
    while(first_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        first_name=(str)(input("MOTHER'S_FIRST_NAME:"))
    last_name=(str)(input("MOTHER'S_LAST_NAME:"))
    while(last_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        last_name=(str)(input("MOTHER'S_LAST_NAME:"))
    mother_name=first_name+" "+last_name#ACCOUNT HOLDER'S MOTHER NAME
    z=True
    x=1
    while z:
        try:
            d1,m1,y1=[int(x) for x in input("ENTER THE DATE OF BIRTH(DD/MM/YYYY):").split('/')]#DOB OF ACCOUNT HOLDER
            dob=date(y1,m1,d1)
            
            x=1
        except ValueError:
            print("ENTER A VALID DATE AS SUGGESTED")
            x=0
        if(x!=0):
            z=False
    dob=date(y1,m1,d1)
    dob=(str)(dob)
    first_name=(str)(input("NOMINEE_FIRST_NAME:"))
    while(first_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        first_name=(str)(input("NOMINEE_FIRST_NAME:"))
    last_name=(str)(input("NOMINEE_LAST_NAME:"))
    while(last_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        last_name=(str)(input("NOMINEE_LAST_NAME:"))
    nom_name=first_name+" "+last_name#ACCOUNT HOLDER'S NOMINEE NAME
    z=True
    while z:
        aad_no=(str)(input("ENTER YOUR AADHAAR NUMBER:"))
        if((aad_no.isdigit())and(len(aad_no)==12)):
            z=False
        else:
            print("PLEASE ENTER A VALID AADHAAR NUMBER.")#AADHAAR NUMBER OF ACCOUNT HOLDER
    z=True
    while z:
        a_pan_no=(str)(input("ENTER YOUR PAN NUMBER:"))
        if((a_pan_no.isalnum())and(len(a_pan_no)==10)):
            z=False
        else:
            print("PLEASE ENTER A VALID PAN NUMBER.")#ACCOUNT HOLDER'S PAN NUMBER
    z=True
    while z:
        g_pan_no=(str)(input("ENTER GUARDIAN'S PAN NUMBER:"))
        if((g_pan_no.isalnum())and(len(g_pan_no)==10)):
            z=False
        else:
            print("PLEASE ENTER A VALID PAN NUMBER.")#GUARDIAN'S PAN NUMBER
    z=True
    while z:
        ph_no=(str)(input("PERMANENT PHONE NUMBER(+91):"))
        if(ph_no.isdigit()and(len(ph_no)==10)):
            z=False
        else:
            print("PLEASE ENTER A VALID PERMANENT PHONE NUMBER.")#ACCOUNT HOLDER'S PERMANENT PHONE NUMBER
    z=True
    while z:
        ph_no2=(str)(input("TEMPORARY PHONE NUMBER:"))
        if(ph_no2.isdigit()and(len(ph_no2)==10)):
            z=False
        else:
            print("PLEASE ENTER A VALID TEMPORARY PHONE NUMBER.")#ACCOUNT HOLDER'S SECONDARY PHONE NUMBER
    pha=(str)(input("ENTER YOUR PERMANENT HOUSE ADDRESS:"))#ACCOUNT HOLDER'S PERMANENT HOUSE ADDRESS
    sha=(str)(input("ENTER YOUR SECONDARY HOUSE ADDRESS:"))#ACCOUNT HOLDER'S SECONDARY HOUSE ADDRESS
    first_name=(str)(input("ACCOUNT_HOLDER'S_GARENTAR'S_FIRST_NAME:"))
    while(first_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        first_name=(str)(input("ACCOUNT_HOLDER'S_GARENTAR'S_FIRST_NAME:"))
    last_name=(str)(input("ACCOUNT_HOLDER'S_GARENTAR'S_LAST_NAME:"))
    while(last_name.isalpha()==False):
        print("PLEASE ENTER A VALID NAME.")
        last_name=(str)(input("ACCOUNT_HOLDER'S_GARENTAR'S_LAST_NAME:"))
    acc_hol_gr_name=first_name+" "+last_name#ACCOUNT HOLDER'S GARENTAR'S NAME
    acc_no=(str)(math.log((int)(ph_no)))
    acc_no=acc_no[4:len(acc_no)]#HERE ACCOUNT NUMBER IS THE logarithm OF THE PERMANENT PHONE NUMBER
    print("YOUR ACCOUNT NUMBER:",acc_no)
    data_saver="INSERT INTO CREATE_BANK_ACCOUNT VALUES("+"'"+acc_hol_name+"'"+","+"'"+father_husband_name+"'"+","+"'"+mother_name+"'"
    data_saver+=","+"'"+dob+"'"+","+"'"+nom_name+"'"+","+"'"+aad_no+"'"+","+"'"+a_pan_no+"'"+","+"'"
    data_saver+=g_pan_no+"'"+","+"'"+ph_no+"'"+","+"'"+ph_no2+"'"+","+"'"+pha+"'"+","+"'"+sha+"'"+","+"'"+acc_hol_gr_name+"'"
    data_saver+=","+"'"+acc_no+"'"+")"
    cursor.execute(data_saver)
    conn.commit()
    z=True
    while z:
        s=(str)(input("DO YOU WANT TO CREATE ANOTHER BANK ACCOUNT(YES OR NO):"))
        s=s.upper()
        if((s=="YES")or(s=="NO")):
            z=False
        else:
            print("ENTER A VALID CHOICE")
    if(s=="YES"):
        print("~"*134*2)
        CR_BA_AC()
    if(s=="NO"):
        print("~"*134*2)
        main_menu()
#______________________________________________________________________________________________        
def DE_CA():
    cr_bal=0.0
    z=True
    while z:
        ph_no=(str)(input("PERMANENT PHONE NUMBER:"))
        if(ph_no.isdigit()and(len(ph_no)==10)):
            z=False
        else:
            print("PLEASE ENTER A VALID PERMANENT PHONE NUMBER.")
    acc_no=(str)(math.log((int)(ph_no)))
    acc_no=acc_no[4:len(acc_no)]
    acc_no=(int)(acc_no)
    cursor.execute("SELECT ACC_NO FROM CREATE_BANK_ACCOUNT")
    acc_no_checker=cursor.fetchall()
    c=0
    for i in acc_no_checker:
        if((int)(i[0])==acc_no):#HERE [0] BECAUSE I IS IN TUPLE FORM AND [0] MEANS 0TH ELEMENT OF I WHICH IS THE WHOLE ACCOUNT NUMBER
            c=1
    if(c==1):
        pass
    else:
        print("INVALID ACCOUNT NOT PRESENT")
        print("FIRST CREATE BANK ACCOUNT")
        main_menu()
    ca=(str)(input("ENTER THE AMOUNT OF CASH TO DEPOSIT:"))#CASH DEPOSITED
    while(ca.isdigit()==False):
        print("PLEASE ENTER A VALID AMOUNT OF CASH.")
        ca=(str)(input("ENTER THE AMOUNT OF CASH TO DEPOSIT:"))
    k=0
    if((int)(ca)>=40000):
        k=1
        z=True
        while z:
            a_pan_no=(str)(input("ENTER YOUR PAN NUMBER:"))
            if((a_pan_no.isalnum())and(len(a_pan_no)==10)):
                z=False
            else:
                print("PLEASE ENTER A VALID PAN NUMBER.")
        s="SELECT ACC_PAN_NO FROM CREATE_BANK_ACCOUNT WHERE ACC_NO="+"'"+((str)(acc_no))+"'"
        cursor.execute(s)
        acc_pan_no_checker=cursor.fetchall()
        c=0
        for i in acc_pan_no_checker:
            if((int)(i[0])==(int)(a_pan_no)):#HERE [0] BECAUSE I IS IN TUPLE FORM AND [0] MEANS 0TH ELEMENT OF I WHICH IS THE WHOLE ACC NO
                 c=1
        if(c==1):
            pass
        else:
            print("INVALID PAN NUMBER NOT PRESENT")
            print("DUE SAFETY REASON YOU ARE DIRECTED TO MAIN MENU.")
            main_menu()
    dat=tim=''
    dat=date.today()
    tim=datetime.now()
    time=tim.strftime("%H:%M:%S")
    tim=(str)(time)
    cursor.execute("SELECT DATE FROM CASH_WITHDRAWL WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
    date_wi=list(cursor.fetchall())
    date_wi.sort()
    cursor.execute("SELECT DATE FROM CASH_DEPOSIT WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
    date_de=list(cursor.fetchall())
    date_de.sort()
    if(len(date_wi)!=0)and(len(date_de)!=0):
        if((date_de[-1])>=(date_wi[-1])):
           cursor.execute("SELECT CURRENT_BALANCE FROM CASH_DEPOSIT WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
           cr_bal=list(cursor.fetchall())
           if(len(cr_bal)>0):
               y=cr_bal[-1]
               cr_bal=(float)(y[0])
           elif(len(cr_bal)==0):
               cr_bal=0.0
           else:
               pass
        else:
           cursor.execute("SELECT CURRENT_BALANCE FROM CASH_WITHDRAWL WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
           cr_bal=list(cursor.fetchall())
           y=cr_bal[-1]
           cr_bal=(float)(y[0])
    elif((len(date_wi)==0)and(len(date_de)!=0)):
           cursor.execute("SELECT CURRENT_BALANCE FROM CASH_DEPOSIT WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
           cr_bal=list(cursor.fetchall())
           y=cr_bal[-1]
           cr_bal=(float)(y[0])
    elif((len(date_wi)==0)and(len(date_de)==0)):
        cr_bal==0.0
    else:
        pass
    if(k==1):
        data_saver="INSERT INTO CASH_DEPOSIT VALUES("+"'"+(str)(acc_no)+"'"+","+"'"+ca+"'"+","+"'"+str(cr_bal+(float)(ca))
        data_saver+="'"+","+"'"+a_pan_no+"'"+","+"'"+(str)(dat)+"'"+","+"'"+tim+"')"
        data_saver1="INSERT INTO PASSBOOK VALUES("+"'"+(str)(acc_no)+"'"+","+"'"+ca+"'"+","+"'NULL'"+","+"'"+str(cr_bal+(float)(ca))
        data_saver1+="'"+","+"'"+a_pan_no+"'"+","+"'"+(str)(dat)+"'"+","+"'"+tim+"')"
    else:
        data_saver="INSERT INTO CASH_DEPOSIT VALUES("+"'"+(str)(acc_no)+"'"+","+"'"+ca+"'"+","+"'"+str(cr_bal+(float)(ca))
        data_saver+="'"+","+"'"+"NULL"+"'"+","+"'"+(str)(dat)+"'"+","+"'"+tim+"')"
        data_saver1="INSERT INTO PASSBOOK VALUES("+"'"+(str)(acc_no)+"'"+","+"'"+ca+"'"+","+"'NULL'"+","+"'"+str(cr_bal+(float)(ca))
        data_saver1+="'"+","+"'"+"NULL"+"'"+","+"'"+(str)(dat)+"'"+","+"'"+tim+"')"
    cursor.execute(data_saver)
    cursor.execute(data_saver1)
    conn.commit()
    z=True
    while z:
        s=(str)(input("DO YOU WANT TO DEPOSIT MORE MONEY(YES OR NO):"))
        s=s.upper()
        if((s=="YES")or(s=="NO")):
            z=False
        else:
            print("INVALID CHOICE.")
    if(s=="YES"):
        print("~"*134*2)
        DE_CA()
    if(s=="NO"):
        print("~"*134*2)
        main_menu()
#_______________________________________________________________________________________________
def CA_WI():
    cr_bal=0.0
    z=True
    while z:
        ph_no=(str)(input("PERMANENT PHONE NUMBER:"))
        if(ph_no.isdigit()and(len(ph_no)==10)):
            z=False
        else:
            print("PLEASE ENTER A VALID PERMANENT PHONE NUMBER.")
    acc_no=(str)(math.log((int)(ph_no)))
    acc_no=acc_no[4:len(acc_no)]
    acc_no=(int)(acc_no)
    cursor.execute("SELECT ACC_NO FROM CREATE_BANK_ACCOUNT")
    acc_no_checker=cursor.fetchall()
    c=0
    for i in acc_no_checker:
        if((int)(i[0])==acc_no):#HERE [0] BECAUSE I IS IN TUPLE FORM AND [0] MEANS 0TH ELEMENT OF I WHICH IS THE WHOLE ACCOUNT NUMBER
            c=1
    if(c==1):
        pass
    else:
        print("INVALID ACCOUNT NOT PRESENT")
        print("FIRST CREATE BANK ACCOUNT")
        main_menu()
    ca=(str)(input("ENTER THE AMOUNT OF CASH TO WITHDRAW:"))#CASH DEPOSITED
    while(ca.isdigit()==False):
        print("PLEASE ENTER A VALID AMOUNT OF CASH.")
        ca=(str)(input("ENTER THE AMOUNT OF CASH TO WITHDRAW:"))
    k=0
    if((int)(ca)>=40000):
        k=1
        z=True
        while z:
            a_pan_no=(str)(input("ENTER YOUR PAN NUMBER:"))
            if((a_pan_no.isalnum())and(len(a_pan_no)==10)):
                z=False
            else:
                print("PLEASE ENTER A VALID PAN NUMBER.")
        s="SELECT ACC_PAN_NO FROM CREATE_BANK_ACCOUNT WHERE ACC_NO="+"'"+((str)(acc_no))+"'"
        cursor.execute(s)
        acc_pan_no_checker=cursor.fetchall()
        c=0
        for i in acc_pan_no_checker:
            if((int)(i[0])==(int)(a_pan_no)):#HERE [0] BECAUSE I IS IN TUPLE FORM AND [0] MEANS 0TH ELEMENT OF I WHICH IS THE WHOLE ACC NO
                 c=1
        if(c==1):
            pass
        else:
            print("INVALID PAN NUMBER NOT PRESENT")
            print("DUE SAFETY REASON YOU ARE DIRECTED TO MAIN MENU.")
            main_menu()
    dat=tim=''
    dat=date.today()
    tim=datetime.now()
    time=tim.strftime("%H:%M:%S")
    tim=(str)(time)
    cursor.execute("SELECT DATE FROM CASH_WITHDRAWL WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
    date_wi=list(cursor.fetchall())
    date_wi.sort()
    cursor.execute("SELECT DATE FROM CASH_DEPOSIT WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
    date_de=list(cursor.fetchall())
    date_de.sort()
    if(len(date_wi)!=0)and(len(date_de)!=0):
        if((date_de[-1])>=(date_wi[-1])):
           cursor.execute("SELECT CURRENT_BALANCE FROM CASH_DEPOSIT WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
           cr_bal=list(cursor.fetchall())
           if(len(cr_bal)>0):
               y=cr_bal[-1]
               cr_bal=(float)(y[0])
           elif(len(cr_bal)==0):
               cr_bal=0.0
           else:
               pass
        else:
           cursor.execute("SELECT CURRENT_BALANCE FROM CASH_WITHDRAWL WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
           cr_bal=list(cursor.fetchall())
           y=cr_bal[-1]
           cr_bal=(float)(y[0])
    elif((len(date_wi)==0)and(len(date_de)!=0)):
           cursor.execute("SELECT CURRENT_BALANCE FROM CASH_DEPOSIT WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
           cr_bal=list(cursor.fetchall())
           y=cr_bal[-1]
           cr_bal=(float)(y[0])
    elif((len(date_wi)==0)and(len(date_de)==0)):
        cr_bal==0.0
    else:
        pass
    if(k==1):
        data_saver="INSERT INTO CASH_WITHDRAWL VALUES("+"'"+(str)(acc_no)+"'"+","+"'"+ca+"'"+","+"'"+str(cr_bal-(float)(ca))
        data_saver+="'"+","+"'"+a_pan_no+"'"+","+"'"+(str)(dat)+"'"+","+"'"+tim+"')"
        data_saver1="INSERT INTO PASSBOOK VALUES("+"'"+(str)(acc_no)+"'"+","+"'NULL'"+","+"'"+ca+"'"+","+"'"
        data_saver1+=str(cr_bal-(float)(ca))+"'"+","+"'"+a_pan_no+"'"+","+"'"+(str)(dat)+"'"+","+"'"+tim+"')"
    else:
        data_saver="INSERT INTO CASH_WITHDRAWL VALUES("+"'"+(str)(acc_no)+"'"+","+"'"+ca+"'"+","+"'"+str(cr_bal-(float)(ca))
        data_saver+="'"+","+"'"+"NULL"+"'"+","+"'"+(str)(dat)+"'"+","+"'"+tim+"')"
        data_saver1="INSERT INTO PASSBOOK VALUES("+"'"+(str)(acc_no)+"'"+","+"'NULL'"+","+"'"+ca+"'"+","+"'"
        data_saver1+=str(cr_bal-(float)(ca))+"'"+","+"'"+"NULL"+"'"+","+"'"+(str)(dat)+"'"+","+"'"+tim+"')"
    cursor.execute(data_saver)
    cursor.execute(data_saver1)
    conn.commit()
    z=True
    while z:
        s=(str)(input("DO YOU WANT TO WITHDRAW MORE MONEY(YES OR NO):"))
        s=s.upper()
        if((s=="YES")or(s=="NO")):
            z=False
        else:
            print("INVALID CHOICE.")
    if(s=="YES"):
        print("~"*134*2)
        CA_WI()
    if(s=="NO"):
        print("~"*134*2)
        main_menu()
#______________________________________________________________________________________________            
def PR_PA():
    z=True
    while z:
        ph_no=(str)(input("PERMANENT PHONE NUMBER:"))
        if(ph_no.isdigit()and(len(ph_no)==10)):
            z=False
        else:
            print("PLEASE ENTER A VALID PERMANENT PHONE NUMBER.")
    acc_no=(str)(math.log((int)(ph_no)))
    acc_no=acc_no[4:len(acc_no)]
    acc_no=(int)(acc_no)
    cursor.execute("SELECT ACC_NO FROM CREATE_BANK_ACCOUNT")
    acc_no_checker=cursor.fetchall()
    c=0
    for i in acc_no_checker:
        if((int)(i[0])==acc_no):#HERE [0] BECAUSE I IS IN TUPLE FORM AND [0] MEANS 0TH ELEMENT OF I WHICH IS THE WHOLE ACCOUNT NUMBER
            c=1
    if(c==1):
        pass
    else:
        print("INVALID ACCOUNT NOT PRESENT")
        print("FIRST CREATE BANK ACCOUNT")
        main_menu()
    cursor.execute("SELECT * FROM CREATE_BANK_ACCOUNT WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
    cba=cursor.fetchall()
    cba1=cba[0]#BECAUSE INSIDE A LIST THERE IS A SINGLE TUPLE OF MANY ELEMENT[(1,2,3,4,5)]
    print("ACCOUNT HOLDER'S NAME:",cba1[0])
    print("FATHER'S/HUSBAND'S NAME:",cba1[1])
    print("MOTHER'S NAME:",cba1[2])
    print("DATE OF BIRTH:",cba1[3])
    print("NOMINEE'S NAME:",cba1[4])
    print("AADHAAR NUMBER:",cba1[5])
    print("ACCOUNT HOLDER'S PAN NUMBER:",cba1[6])
    print("ACCOUNT HOLDER'S GUARDIAN'S PAN NUMBER:",cba1[7])
    print("PERMANENT PHONE NUMBER:",cba1[8])
    print("TEMPORARY PHONE NUMBER:",cba1[9])
    print("PERMANENT HOUSE ADDRESS:",cba1[10])
    print("TEMPORARY HOUSE ADDRESS:",cba1[11])
    print("GARENTER'S NAME:",cba1[12])
    print("ACCOUNT NUMBER:",cba1[13])
    cursor.execute("SELECT * FROM PASSBOOK WHERE ACC_NO="+"'"+(str)(acc_no)+"'")
    pb=cursor.fetchall()
    rows=cursor.rowcount
    print("ACCOUNT NUMBER     CASH DEPOSITED   CASH WITHDRAWN   CURRENT BALANCE   PAN NUMBER   DATE          TIME")
    for i in pb:
        acc_no=i[0]
        cd=i[1]
        cw=i[2]
        cb=i[3]
        pn=i[4]
        date=i[5]
        time=i[6]
        print(acc_no,"   ",cd," "*(15-len(cd)),cw," "*(15-len(cw)),cb," "*(16-len(cb)),pn," "*(11-len(pn)),date,"  ",time)
    z=True
    while z:
        s=(str)(input("DO YOU WANT TO PRINT ANOTHER PASSBOOK(YES OR NO):"))
        s=s.upper()
        if((s=="YES")or(s=="NO")):
            z=False
        else:
            print("ENTER A VALID CHOICE")
    if(s=="YES"):
        print("~"*134*2)
        PR_PA()
    if(s=="NO"):
        print("~"*134*2)
        main_menu()
          
main_menu()

