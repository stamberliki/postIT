#! /Python34/python.exe
print("Content-type:text/html\n")

import cgi, cgitb, pymysql, os
cgitb.enable()
conn=pymysql.connect(host='localhost', user='root', password='', db='webdev2')
cursor = conn.cursor()

form = cgi.FieldStorage()

fileitem = form['pic']
caption = form.getvalue('caption')

fn = os.path.basename(fileitem.filename)
open('../images/' + fn, 'wb').write(fileitem.file.read())
message = 'The file "' + fn + '" was uploaded successfully'
query = "insert into imahe(imgName,caption) values (%s,%s)"
cursor.execute(query,(fn,caption))
conn.commit()

print ("""
<html>
<body>
   <p>""")
print(message)
print("""</p>
	<a href="../prototype.py">back</a>
</body>
</html>
""")
conn.close()