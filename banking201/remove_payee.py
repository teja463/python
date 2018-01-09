#!"C:\\Program Files\\Python36\\python.exe"

import cgi, cgitb
from database import Account
from html import *

print_body()

form = cgi.FieldStorage()

ac_no = form.getvalue("ac_no")
ac_name = form.getvalue("ac_name")
ac_bank = form.getvalue("ac_bank")

status = Account.remove_payee(ac_no, ac_bank)

if status:
    print_alert_msg("Payee deleted successfully", "info")