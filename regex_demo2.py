import re

# IP Address validation

ip = input("Enter a IP Address: ")

if (re.search("^(\d{1,3}[.]){3}\d{1,3}$",ip)):
    print ("valid id address")
else:
    print ("Invalid ip adddress")

aadhar_str = input("Enter a string with aadhar details: ")

if(re.search("(\d{4}\s){2}\d{4}",aadhar_str)):
    print ("valid aadhar")
else:
    print ("invalid aadhar")


aadhar = re.findall("\d{4}\s\d{4}\s\d{4}",aadhar_str)

print ("aadhar: ", aadhar)


abc='guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
emails = re.findall('[\w\.-]+@[\w\.-]+', abc) 
for email in emails:
    print (email)
