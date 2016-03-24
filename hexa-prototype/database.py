import sqlite3
import os.path

conn = sqlite3.connect('hexaproto.db')

def createtables():
    conn = sqlite3.connect('hexaproto.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE CUST
       (ID INT PRIMARY KEY     NOT NULL,
       PHN CHAR(10) NOT NULL UNIQUE,
       NAME           TEXT,
       EMAIL        CHAR(50),
       BAL         REAL);''')
    print("Cust Table created successfully")
    conn.execute('''CREATE TABLE LOGS
       (TRANSID INT PRIMARY KEY     NOT NULL,
       ID INT   NOT NULL,
       TRANSTYPE CHAR NOT NULL,
       AMT         REAL NOT NULL);''')
    print("LOGS Table created successfully")
    conn.close()

def reguser(id, phn, bal, name='NULL', email='NULL'):
    conn = sqlite3.connect('hexaproto.db')
    print("Opened database successfully")
    conn.execute("INSERT INTO CUST (ID,PHN,NAME,EMAIL,BAL) \
      VALUES (?, ?, ?, ?, ? )" ,(id, phn, name, email, bal))
    conn.commit()
    trans(id,bal,'+')
    conn.commit()
    print("Records created successfully")
    conn.close()

def trans(id,amt,ttype):
    conn = sqlite3.connect('hexaproto.db')
    print("Opened database successfully")
    s = "SELECT BAL from CUST WHERE ID = %d" % id
    cursor = conn.execute(s)
    for row in cursor:
        bal=row[0]
    if(ttype == '-'):
        if(bal<amt):
            conn.close()
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
    conn.close()
    return 1

def getbal(id):
    conn = sqlite3.connect('hexaproto.db')
    print("Opened database successfully")
    s = "SELECT BAL from CUST WHERE ID = %d" % id
    cursor = conn.execute(s)
    for row in cursor:
        bal=row[0]
        conn.close()
        return bal
    conn.close()
    return -1


def disp_all():
    #conn = sqlite3.connect('hexaproto.db')
    print("Opened database successfully")
    cursor = conn.execute("SELECT *  from CUST")
    for row in cursor:
        print("ID = ", row[0])
        print("PHN = ", row[1])
        print("NAME = ", row[2])
        print("EMAIL = ", row[3])
        print("BAL = ", row[4]), "\n"
    print("Operation done successfully")
    #conn.close()


#conn.execute('''.schema LOGS''')
#trans(101,10,'+')
#reguser(102,'7790844832',550)
#disp_all()
#print(getbal(100))


#conn.close()