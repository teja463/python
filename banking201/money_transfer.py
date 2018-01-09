#!"C:\\Program Files\\Python36\\python.exe"

import cgi, cgitb
from database import Account
from database import Authentication
from html import *

print_body()

form = cgi.FieldStorage()

ac_no = form.getvalue("ac_no")
ac_bank = form.getvalue("ac_bank")
amount = form.getvalue("amount")

status = Account.money_transfer(ac_no, ac_bank, amount)

if status:
    print_alert_msg ("Money transfered and balance updated successfully","info")
else:
    msg = "There are no records exists with Account no {}".format(ac_no)
    print_alert_msg(msg, "danger")
