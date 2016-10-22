#! /Python34/python.exe
print("Content-type:text/html\n")

import cgi, cgitb
cgitb.enable()

file = open("session.txt","r+")

print("""
<html>
<head>
<meta http-equiv="refresh" content="0;url=../prototype.py">
</head>
<body>
""")

file.seek(0,0)
file.write("login: 0")

print("""
</body>
</html>
	""")
file.close()