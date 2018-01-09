#!"C:\\Program Files\\Python36\\python.exe"

import cgi, cgitb
from database import Authentication
import logging
from html import *

logger = logging.getLogger(__name__)

print_body()
form = cgi.FieldStorage()

ac_no = form.getvalue("ac_no")
ac_name = form.getvalue("ac_name")
ac_branch = form.getvalue("ac_branch")
paswd = form.getvalue("paswd")

status = Authentication.register_user(ac_no,ac_name,ac_branch,paswd)

def print_success():
    print_alert_msg ("User {} has been register successfully you can login with your account no and password".format(ac_name), "info")
    print ("Click here to <a href='index.html' class='btn btn-info'>Login</a>.")

def print_user_exists():
    print_alert_msg ("User {} is already registered Click here to <a href='index.html' class='btn btn-info'>Login</a>.".format(ac_name), "danger")


def print_no_user():
    print_alert_msg ("There are no details present in our database with account no {} ".format(ac_no), "info")
    print ("<h3> Below are the accounts present. You can register with anyone of the account no</h3>")
    print ("<p>Click here to <a href='register.html' class='btn btn-info'>Register</a> again.</p>")
    res = Authentication.get_all_acc_details()
    rows = res.fetch_row(maxrows=5)
    print ("<table class='table table-hover'><tr><th>Acc No</th><th>Acc Name</th><th>Acc Branch</th>")
    while(rows):
        
        for row in rows:
            print ("<tr>")
            print ("<td>{}</td>".format(str(row[0],'utf-8')))
            print ("<td>{}</td>".format(str(row[1],'utf-8')))
            print ("<td>{}</td>".format(str(row[2],'utf-8')))
            print ("</tr>")
        rows = res.fetch_row(maxrows=5)
    print ("</table>")

if status == "UC":
    print_success()
elif status == "UE":
    print_user_exists()
elif status == "NU":
    print_no_user()



#print_no_user()