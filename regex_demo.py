import re

string = input("Enter a String: ")

# Simple matching

if (re.search('Python', string)): # search for python in string
    print ("Python satisfied")
else:
    print ("Python not satisfied")

if (re.search('python', string, re.I)): # search for pyhton in string ignroe case
    print ("python satisfied")
else:
    print ("python satisfied")

# Anchor types examples

if (re.search("^python", string)): # search for python at the start of the sentence
    print ("^python satisfied")
else:
    print ("^python not satisfied")

if (re.search("python$", string)): # search for python at the end of the sentence
    print ("python$ satisfied")
else:
    print ("python$ not satisfied")

if (re.search("^python$", string)): # input should be only the word python
    print ("^python$ satisfied")
else:
    print ("^python$ not satisfied")
# Range of characters

if (re.search("[0-9][a-z][A-Z]", string)): # Matches any input string which has a three letter word whoose first lette ris num , 2nd small char, 3rd caps char
    print ("[0-9][a-z][A-Z] satisfied")
else:
    print ("[0-9][a-z][A-Z] not satisfied")

if (re.search("^[0-9][a-z][A-Z]$", string)): # input should exactly be a three letter word whoose first lette ris num , 2nd small char, 3rd caps char
    print ("^[0-9][a-z][A-Z]$ satisfied")
else:
    print ("^[0-9][a-z][A-Z]$ not satisfied")
    

        
print ("---------------------------------------------------------------")

# Phone number validation

ph_num = input("Enter a phone number")

# Approach 1

if (re.search("^[789][0-9]{9}", ph_num)):
    print ("Valid phone number")
else:
    print ("Invalid phone number")
    
# Approach 2

if (re.search("^[789]\d{9}", ph_num)):
    print ("Valid phone number")
else:
    print ("Invalid phone number")

# Eamil validation

email = input("Enter email")

# Approach 1

if (re.search("^[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+",email)):
    print ("Valid email")
else:
    print ("Invalid email")

# Approach 2

if (re.search("^\w+@\w+.\w+",email)):
    print ("Valid email")
else:
    print ("Invalid email")

# aadhar validation

aadhar = input("Enter Aadhar id: ")

# Approach 1

if (re.search("^\d{4}\s\d{4}\s\d{4}$", aadhar)):
    print ("Valid aadhar")
else:
    print ("Invalid aadhar")

# Approach 2

if (re.search("^(\d{4}\s){2}\d{4}$", aadhar)):
    print ("Valid aadhar")
else:
    print ("Invalid aadhar")

# PAN verification

pan = input("Enter a PAN: ")

if (re.search("^[A-Z]{5}\d{4}[A-Z]$", pan)):
    print ("Valid PAN")
else:
    print ("Invalid PAN")

# Find All

find_all = re.findall("\d{3}", input("Enter find all string "))
print (find_all, type(find_all))

# Sub

substitute_str = re.sub("\d{3}", "444", input("Enter substitue string "))
print (substitute_str)


