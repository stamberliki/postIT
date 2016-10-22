#! /Python34/python.exe
print("Content-type:text/html\n")

import cgi, cgitb, pymysql
cgitb.enable()

storage = cgi.FieldStorage()

comment = storage.getvalue("comment")
img = storage.getvalue('img')

file = open("session.txt","r+")
file.readline()
user = file.readline().split()
conn=pymysql.connect(host='localhost', user='root', password='', db='webdev2')
cursor = conn.cursor()

cursor.execute('INSERT into comments(comment,imgID,username) values ("'+comment+'","'+img+'","'+user[len(user)-1]+'") ')
conn.commit()

print("""
<html>
<head>
</head>
<body onload="setTimeout(function(){ document.resubmit.submit() },0)">
	<form name="resubmit" action="../comments.py" method="post">
		<input type="hidden" name="comment" value="""+img+""" />
	</form>
</body>
</html>
	""")
file.close()
conn.close()