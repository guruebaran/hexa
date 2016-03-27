__author__ = 'guru'
import sqlite3
import os.path

conn = sqlite3.connect('hexabeta.db')

print("Opened database successfully")


def createtables():
    conn.execute('''CREATE TABLE CustomerDetails
       (MobileNumber CHAR(10) PRIMARY KEY NOT NULL UNIQUE,
       AccountBalance REAL);''')
    print("CustomerDeails Table created successfully")
    conn.execute('''CREATE TABLE TransactionLogs
       (TransactionId INT PRIMARY KEY NOT NULL,
       MobileNumber CHAR(10) NOT NULL,
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
       AccessPin INT );''')
    print("vendor details Table created successfully")

def registerVendor(VendorId, VendorName = "NULL", VendorBalance = 0.00):
    conn.execute("INSERT INTO VendorDetails (VendorId, VendorName, VendorBalance) \
      VALUES (?, ?, ?)", (VendorId, VendorName, VendorBalance))
    conn.commit()
    print("Vendor created successfully")

def registerVendingUser(UserId, VendorId, AccessPin):
    conn.execute("INSERT INTO VendorDetails (UserId, VendorId, AccessPin) \
      VALUES (?, ?, ?)", (UserId, VendorId, AccessPin))
    conn.commit()
    print("Vending user created successfully")

def createVendorLog(LogId, DeviceId, VendorId, UserId, DateTime):
    conn.execute("INSERT INTO VendorDetails (LogId, DeviceId, VendorId, UserId, DateTime) \
      VALUES (?, ?, ?, ? ,?)", (LogId, DeviceId, VendorId, UserId, DateTime))
    conn.commit()
    print("Vendor log created successfully")

def registerUser (MobileNumber, VendorId, AccountBalance = 0):
    conn.execute("INSERT INTO CustomerDetails (MobileNumber,AccountBalance) \
      VALUES (?, ?)", (MobileNumber, 0))
    conn.commit()
    trans(MobileNumber, AccountBalance, '+', VendorId)
    conn.commit()
    print("Records created successfully")

def trans(MobileNumber,Amount,TransactionType, VendorId):
    currentBalance=getbal(MobileNumber)
    if(TransactionType == '-'):
        if(currentBalance<Amount):
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
    DateTime = getDateTime()
    conn.execute("INSERT INTO TransactionLogs (TransactionId,MobileNumber,TransactionType, DateTime, VendorId ,Amount) \
      VALUES (?, ?, ?, ?, ?,     ? )",(tid, MobileNumber, TransactionType, DateTime, VendorId, Amount))
    if (TransactionType == '+'):
        t = currentBalance + Amount
        #s = "UPDATE CustomerDetails SET AccountBalance = %d WHERE MobileNumber = '{!s}'" .format(t, MobileNumber)
        conn.execute("UPDATE CustomerDetails SET AccountBalance = ? WHERE MobileNumber = ?",(t, MobileNumber))
    elif(TransactionType == '-'):
        t = currentBalance - Amount
        #s = "UPDATE CustomerDetails SET AccountBalance = %d WHERE MobileNumber = '{!s}'" .format(t, MobileNumber)
        conn.execute("UPDATE CustomerDetails SET AccountBalance = ? WHERE MobileNumber = ?",(t, MobileNumber))
    conn.commit()
    print("Records created successfully id = %d"%(tid))
    return 1

def getDateTime():
    for row in conn.execute('SELECT datetime("now","localtime")'):
        return row[0]

def getbal(MobileNumber):
    s = "SELECT AccountBalance from CustomerDetails WHERE MobileNumber = %s" % MobileNumber
    cursor = conn.execute(s)
    for row in cursor:
        return row[0]
    return -1

def displayAllTransactionLogs():
    cursor = conn.execute("SELECT *  from TransactionLogs")
    for row in cursor:
        print("\nTransactionId = ", row[0])
        print("MobileNumber = ", row[1])
        print("TransactionType = ", row[2])
        print("DateTime = ", row[3])
        print("VendorId = ", row[4])
        print("Amount = ", row[5])
    print("Operation done successfully")

def displayAllCustomerDetails():
    cursor = conn.execute("SELECT *  from CustomerDetails")
    for row in cursor:
        print("\nMobileNumber = ", (row[0]))
        print("AccountBalance = ", (row[1]))
    print("Operation done successfully")



#createtables()
#conn.execute('''.schema LOGS''')
#trans("7790844870",100,'+',1001)
#registerUser("7790844870",500, 1001)
#registerVendor(1001,"Tuck Shop", 0)

displayAllTransactionLogs()
#print(getbal("7790844870"))
displayAllCustomerDetails()
conn.close()