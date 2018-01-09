#!"C:\\Program Files\\Python36\\python.exe"

import cgi, cgitb
from database import Account
from database import Authentication
from html import *

print_body()
form = cgi.FieldStorage()

ac_no = form.getvalue("ac_no")
ac_name = form.getvalue("ac_name")
ac_bank = form.getvalue("ac_bank")

st, msg = Account.add_payee(ac_no, ac_name, ac_bank)
print_alert_msg(msg, "info")
def print_no_user():
    print ("<h3> Below are the accounts present. You can add payee with anyone of the account no</h3> <br/>")
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

if not st:
    print_no_user()