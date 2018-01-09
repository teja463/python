#!"C:\\Program Files\\Python36\\python.exe"

import cgi, cgitb
from database import Authentication
import logging
from html import *

logger = logging.getLogger(__name__)
print_body()
print_logout()
form = cgi.FieldStorage()

ac_no = form.getvalue("ac_no")
paswd = form.getvalue("paswd")

def show_acc_details(ac_no):
    logger.debug("Showing account details for {}".format(ac_no))
    details = Authentication.get_acc_details(ac_no)
    a_no, a_name, a_branch, a_bank, a_bal = str(details[0],'utf-8'),str(details[1],'utf-8'),str(details[2],'utf-8'),str(details[3],'utf-8'),details[4]
    print_heading("Welcome " +a_name)
    print ('''
        <table class='table table-hover'>
            <thead class="thead-light">
            <tr>
                <th>Account Name</th>
                <th>Balance</th>
                <th>Account Number</th>
            </tr>
            </thead>
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            <tr>
                <td><a href='add_payee.html' class='btn btn-info'>Add Payee</a></td>
                <td><a href='remove_payee.html' class='btn btn-info'>Remove Payee</a></td>
                <td><a href='money_transfer.html' class='btn btn-info'>Money Transfer</a></td>
                
            </tr>
             <tr>
                <td colspan=3 align='center'><a href='deposit.html' class='btn btn-info'>Deposit Money</a></td>
            </tr>
        </table>
        '''.format(a_name,a_bal,a_no))


if Authentication.login(ac_no,paswd):
    #print ("<h2> Account number {} Password {}</h2>".format(ac_no, paswd))
    show_acc_details(ac_no)
else:
    logger.debug("Invalid details ac_no {} paswd {}".format(ac_no,paswd))
    print_alert_msg("Invalid login try again", "danger")
    print ("<a href='index.html' class='btn btn-info'>Back to Login</a>")

