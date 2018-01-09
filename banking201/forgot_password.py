#!"C:\\Program Files\\Python36\\python.exe"

import cgi, cgitb
from database import Authentication
from html import *

print_body()
form = cgi.FieldStorage()

ac_no = form.getvalue("ac_no")
paswd = form.getvalue("paswd")

Authentication.update_password(ac_no,paswd)

print_alert_msg ("Password Updated Successfully", "info")
print ("<a href='index.html' class='btn btn-info'>Back to Login</a>")