#!"C:\\Program Files\\Python36\\python.exe"

def print_body():
    print ("Content-Type: text/html")
    print ("""
        <html>
        <title> Dashboard </title>
        <head>
            <script type="text/javascript" src="js/jquery-3.2.1.min.js"></script>
            <link rel="stylesheet" href="css/bootstrap.min.css">
            <script src="js/bootstrap.min.js"></script>
        </head>
        <body class="container">
        <h2>My Banking Application </h2>
    """)

def print_heading(mod_name):
    print ("<div  class='page-header'> <h3> {} </h3></div>".format(mod_name))

def print_alert_msg(msg, css_class):
    print ("<div class='alert alert-{}'> {} </div>".format(css_class, msg))

def print_logout():
    print ('<div class="row col-md-offset-11"><a href="index.html" class="btn btn-danger">Logout</a></div>')