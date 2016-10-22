#! /Python34/python.exe
print("Content-type:text/html\n")

import cgi, cgitb, pymysql
cgitb.enable()

storage = cgi.FieldStorage()

username = storage.getvalue("username")
password = storage.getvalue("password")

conn=pymysql.connect(host='localhost', user='root', password='', db='webdev2')
cursor = conn.cursor()

cursor.execute("SELECT * FROM profiles where username ='"+username+"' and password ='"+password+"'")

file = open("session.txt","w+")
file.write("login: 0")
if len(cursor.fetchall()) == 1:
	print("""
<html>
<head>
<meta http-equiv="refresh" content="0;url=../prototype.py">
</head>
<body>
""")
	file.seek(0,0)
	file.write("login: 1\n")
	file.write("username: "+username+"\n")

	print("""
</body>
</html>
	""")
else:
	print("""
<html>
<head>
<meta http-equiv="refresh" content="3;url=../prototype.py">
</head>
<body>
Login failed. Redirecting to Home page in 3 seconds.
</body>
</html>
	""")
file.close()
conn.close()