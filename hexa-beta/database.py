__author__ = 'guru'
import sqlite3
import os.path

conn = sqlite3.connect('hexabeta.db')

print("Opened database successfully")


def createtables():
    conn.execute('''CREATE TABLE CustomerDetails
       (AccountId INT PRIMARY KEY NOT NULL,
       MobileNumber CHAR(10) NOT NULL UNIQUE,
       FPId1         INT,
       FPId2         INT,
       AccountBalance REAL);''')
    print("CustomerDeails Table created successfully")
    conn.execute('''CREATE TABLE TransactionLogs
       (TransactionId INT PRIMARY KEY NOT NULL,
       AccountId INT   NOT NULL,
       TransactionType CHAR NOT NULL,
       DateTime TEXT NOT NULL,
       VendorId INT NOT NULL,
       Amount REAL NOT NULL);''')
    print("transaction logs Table created successfully")
    conn.execute('''CREATE TABLE VendorLogs
       (LogId INT PRIMARY KEY NOT NULL,
       DeviceId INT NOT NULL,
       VendorId INT NOT NULL,
       UserId INT NOT NULL,
       DateTime TEXT NOT NULL);''')
    print("vendor logs Table created successfully")
    conn.execute('''CREATE TABLE VendorDetails
       (VendorId INT PRIMARY KEY     NOT NULL,
       VendorName CHAR(3) NOT NULL,
       VendorBalance REAL NOT NULL);''')
    print("vendor details Table created successfully")
    conn.execute('''CREATE TABLE VendingUserDetails
       (UserId INT PRIMARY KEY     NOT NULL,
       VendorId INT NOT NULL,
       FPVId1 INT,
       FPVId2 INT,
       VendorBalance REAL );''')
    print("vendor details Table created successfully")

def reguser(id, phn, bal, name='NULL', email='NULL'):
    conn.execute("INSERT INTO CUST (ID,PHN,NAME,EMAIL,BAL) \
      VALUES (?, ?, ?, ?, ? )" ,(id, phn, name, email, bal))
    conn.commit()
    trans(id,bal,'+')
    conn.commit()
    print("Records created successfully")

def trans(id,amt,ttype):
    s = "SELECT AccountBalance from CustomerDetails WHERE AccountId = %d" % id
    cursor = conn.execute(s)
    for row in cursor:
        bal=row[0]
    if(ttype == '-'):
        if(bal<amt):
            return 0
    if (os.path.isfile("transid.dat")):
        fo = open("transid.dat", "rb+")
        tid = fo.read()
        tid = tid.decode('utf-8')
        tid = int(tid)
        tid = tid+1
        fo.seek(0)
        fo.truncate()
        fo.write(bytes(str(tid), 'UTF-8'))
    else:
        fo = open("transid.dat", "ab")
        tid = 1
        fo.write(bytes(str(tid), 'UTF-8'))
    fo.close()
    conn.execute("INSERT INTO LOGS (TRANSID,ID,TRANSTYPE,AMT) \
      VALUES (?, ?, ?, ? )",(tid, id, ttype, amt))
    if (ttype == '+'):
        t = bal+amt
        s = "UPDATE CUST SET BAL = %d WHERE ID = %d" %(t , id)
        conn.execute(s)
    elif(ttype == '-'):
        t = bal-amt
        s = "UPDATE CUST SET BAL = %d WHERE ID = %d" %(t , id)
        conn.execute(s)
    conn.commit()
    print("Records created successfully id = %d"%(tid))
    return 1

def getbal(id):
    s = "SELECT AccountBalance from CustomerDetails WHERE AccountId = %d" % id
    cursor = conn.execute(s)
    for row in cursor:
        bal=row[0]
        return bal
    return -1

def disp_all():
    cursor = conn.execute("SELECT *  from CUST")
    for row in cursor:
        print("ID = ", row[0])
        print("PHN = ", row[1])
        print("NAME = ", row[2])
        print("EMAIL = ", row[3])
        print("BAL = ", row[4]), "\n"
    print("Operation done successfully")


#conn.execute('''.schema LOGS''')
#trans(101,1,'+')
#reguser(101,'7790844803',200)
#disp_all()
#print(getbal(100))

conn.close()