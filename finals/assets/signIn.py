#! /Python34/python.exe
print("Content-type:text/html\n")

import cgi, cgitb, pymysql
cgitb.enable()

storage = cgi.FieldStorage()

username = storage.getvalue("username")
password = storage.getvalue("password")

conn=pymysql.connect(host='localhost', user='root', password='', db='webdev2')
cursor = conn.cursor()

usernameCheck = cursor.execute("SELECT username from profiles where username = '"+username+"'")

print("""
<html>
<head>
<meta http-equiv="refresh" content="3;url=../prototype.py">
</head>
<body>
""")
if usernameCheck == 0:
	cursor.execute("INSERT into profiles(username,password) values ('"+username+"','"+password+"')")
	conn.commit()
	print('Sign in successful. Redirecting in 3 seconds');
else:
	print('Sign in fail. Redirecting in 3 seconds')

print("""
</body>
</html>
	""")