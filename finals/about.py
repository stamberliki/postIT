#! /Python34/python.exe
print("Content-type:text/html\n")

import cgi, cgitb, pymysql
cgitb.enable()

session = open("assets/session.txt","a+")
session.seek(0)
login = session.readline().split() if session.read(1) else [0]

print("""
<html>
<head>
	<title></title>
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
  print("""		<li><a style="color:white;">Welcome """+username[len(username)-1]+"""</a></li>
  					  <li><a style="color:white;" href="logout.py">LOG OUT</a></li>""")
else:
  print("""
    				<li><a data-toggle="modal" href="#signUpModal" style="color: white">SIGN-UP</a></li>
					  <li><a data-toggle="modal" href="#logInModal" style="color: white">LOGIN</a></li>""")
print("""
      			</ul>
    		</div>
  		</div>
	</nav>
  <div class="abtContainer">
    <div class="abtContent">
      <pre><center>
        ABOUT THE WEBSITE:
        Post it! is a social media user-generated content website where you can post, like and
        comment on photos and giving you the power to share amazing things on the internet this days without barriers!
      </center></pre>
    </div>

    <center><h1>PEOPLE BEHIND POST IT!</h1></center>

    <div class="abtContent">
      <pre><center>
        Khryss Bea Ayuste
        Web Designer

        I am Khryss, of house Ayuste. Rightful heir to the Iron Throne, Queen of the Seven Kingdoms of Westeros, the Rhoynar, and the First Men.
        I am the Mother of Dragons, the Khaleesi of the Great Grass Sea, the Unburnt, and Breaker of Chains. I am The Khaleesi.
        </center></pre>
    </div>

    <div class="abtContent">
      <pre><center>
        Christian Jenoel Alorro
        Web Programmer

        Being a programmer is not a simple task, but being a programmer is the most effortless job. You just sit there coding while drinking coffee,
        getting those codes on the internet, and do it again almost everydayself.
      </center></pre>
    </div>

    <div class="abtContent">
      <pre><center>
        Christian Mae Mendez
        Project Manager

        I am Christian Mae of House Mendez, a lion of the Rock, the rightful queen of these Seven Kingdoms, trueborn daughter of Michael and hair grows back..      
        </center></pre>
    </div>
    
    <div class="abtContent">
      <pre><center>
        Jim Salarza
        Web Designer

        Jim of House Salarza, the first of his name. King of Andals, the Rhoynar and the First Men. Lord of the Seven Kingdoms and Protector of the Realm
        </center></pre>
    </div>
    
  </div>
</body>
<link rel="stylesheet" type="text/css" href="css/mainCSS.css">
<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
<script src="css/jquery.min.js"></script>
<script src="css/bootstrap.js"></script>
</html>""")