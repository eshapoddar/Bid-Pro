import sqlite3
import cgi
conn=sqlite3.connect('portal.db')
#conn.execute("CREATE TABLE data (phno VARCHAR PRIMARY KEY, name VARCHAR);")

regList=[]



fname=cgi.FieldStorage().getValue('fname')
password=cgi.FieldStorage().getValue('password')
phno=cgi.FieldStorage().getValue('phno')
lname=cgi.FieldStorage().getValue('lname')
dob=cgi.FieldStorage().getValue('dob')
email=cgi.FieldStorage().getValue('email')
address=cgi.FieldStorage().getValue('address')
sql = ("INSERT INTO customers (name, password,phno) VALUES (%s, %s, %s);")
val = (name,password,phno)
conn.execute(sql, %val)


conn.commit()
conn.close()
