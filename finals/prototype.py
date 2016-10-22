#! /Python34/python.exe
print("Content-type:text/html\n")

import cgi, cgitb, pymysql
cgitb.enable()

conn=pymysql.connect(host='localhost', user='root', password='', db='webdev2')
cursor = conn.cursor()

cursor.execute(""" SELECT * FROM imahe order by imgID DESC""")

session = open("assets/session.txt","a+")
session.seek(0)
login = session.readline().split() if session.read(1) else [0]

print("""
<html>
<head>
	<title></title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
	<div id="logInModal" class="modal fade" role="dialog">
      <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal">&times;</button>
              <h4 class="modal-title">Log in</h4>
            </div>
            <div class="modal-body">
              <form action="assets/login.py" method="post">
                <div class="line">E-mail: <input type="text" name="username"></div>
                <div class="line">Password: <input type="password" name="password"></div>
                <div class="line"><input type="submit" value="Login"></div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
  </div>

  <div id="signUpModal" class="modal fade" role="dialog">
      <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal">&times;</button>
              <h4 class="modal-title">Log in</h4>
            </div>
            <div class="modal-body">
              <form action="assets/signIn.py" method="post">
                <div class="line">E-mail: <input type="text" name="username"></div>
                <div class="line">Password: <input type="password" name="password"></div>
                <div class="line"><input type="submit" value="Sign up"></div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
  </div>

	<div id="postModal" class="modal fade" role="dialog">
  		<div class="modal-dialog">
    		<div class="modal-content">
      			<div class="modal-header">
        			<button type="button" class="close" data-dismiss="modal">&times;</button>
        			<h4 class="modal-title">POST</h4>
      			</div>
      			<div class="modal-body">
					<form method="post" action="assets/imgPost.py" enctype="multipart/form-data">
  						<input type="file" name="pic" accept="image/*" required="required">
      					<div>Caption: <input type="text" name="caption" required="required"></div>
  						<input type="submit" value="Upload">
					</form>
      			</div>
      			<div class="modal-footer">
        			<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      			</div>
		    </div>
  		</div>
	</div>

	<nav class="navbar navbar-default navbar-fixed-top">
  		<div class="container">
    		<div class="navbar-header">
      			<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        			<span class="icon-bar"></span>
        			<span class="icon-bar"></span>
        			<span class="icon-bar"></span>
      			</button>
      			<a class="navbar-brand" href="prototype.py" style="color:#225458;"><img src="logo.png" class="logo"></a>
    		</div>
    		<div class="collapse navbar-collapse" id="myNavbar">
	      		<ul class="nav navbar-nav navbar-right">
        			<li><a href="about.py" style="color: white">ABOUT</a></li>
        			""")

if int(login[len(login)-1]) == 1:
  username = session.readline().split()
  print('<li><a style="color:white;">Welcome '+username[len(username)-1]+'</a></li>')
  print('<li><a style="color:white;" href="assets/logout.py">LOG OUT</a></li>')
else:
  print("""
    <li><a data-toggle="modal" href="#signUpModal" style="color: white">SIGN-UP</a></li>
		<li><a data-toggle="modal" href="#logInModal" style="color: white">LOGIN</a></li>""")
print("""
      			</ul>
    		</div>
  		</div>
	</nav>
	<div class="container1">
  <form method="get" action="comments.py" enctype="multipart/form-data">
""")

for x in cursor.fetchall():
	print("""
		<div class="post">
			<div class="caption">"""+x[2]+"""</div>
			<input class="image" type="image" name="comment" value="""+str(x[0])+""" src="images/"""+x[1]+"""">
		</div>
""")
print('</form>')

if int(login[len(login)-1]) == 1:
  print("""
	<div class="postBtn">
		<a data-toggle="modal" href="#postModal">
			<img src="post.png" id="icon">
		</a>
	</div>
	""")

print("""
	</div>
</body>
<link rel="stylesheet" type="text/css" href="css/mainCSS.css">
<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
<script src="css/jquery.min.js"></script>
<script src="css/bootstrap.js"></script>
</html>
""")
conn.close()