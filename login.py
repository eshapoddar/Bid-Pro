import sqlite3
import cgi
conn=sqlite3.connect('portal.db')
conn.execute("CREATE TABLE data (phno VARCHAR PRIMARY KEY, name VARCHAR);")

regList=[]

cursor=conn.execute("SELECT email, password FROM user")

for i in cursor:
	regList.append(i[0])
name=cgi.FieldStorage().getValue('email')
password=cgi.FieldStorage().getValue('password')

if password in regList:
    if name in regList:
	print ("Success.")
print('Content-Type:text/html \r\n\r\n')
print("<button onclick="category_1_1.html">Next</button>")

conn.commit()
conn.close()
