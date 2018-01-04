# Postional argument Demo

def display_emp_1(name, location, salary):
  print ("name: " , name)
  print ("location: ", location)
  print ("salary: ", salary)
  print ("------------------------------------------------------------------")

display_emp_1("Teja", "Bangalore", 50000)

display_emp_1("Bangalore", "Teja", 50000)

# Keyword arguments Demo

def display_emp_2(name, location, salary):
  print ("name: " , name)
  print ("location: ", location)
  print ("salary: ", salary)
  print ("------------------------------------------------------------------")
display_emp_2(name="Teja", location="Bangalore", salary=50000)

display_emp_2(location="Bangalore", name="Teja", salary=50000)

# Default arguments Demo

def display_emp_3(name, location="Bangalore", salary=10000):
  print ("name: " , name)
  print ("location: ", location)
  print ("salary: ", salary)
  print ("------------------------------------------------------------------")

display_emp_3(name="Teja")
display_emp_3(location="Hyderabad", name="Teja")
display_emp_3(location="Hyderabad", name="Teja", salary=50000)

# None demo

def chk_name(name=None):
    if name is None:
        print ("Name is not passed")
    else:
        print ("Name is: ", name)

chk_name("Teja")
chk_name()
print ("------------------------------------------------------------------")
# Mutliple return values demo
def multi_return(mail_id):
    if(mail_id and mail_id.count("@") == 1):
        return (mail_id,"valid")
    else:
        return (mail_id,"invalid")


mail, status = multi_return("teja463@gmail.com")
print (mail, " -> ", status)

print ("------------------------------------------------------------------")

mail, status = multi_return("teja463")
print (mail, " -> ", status)

print ("------------------------------------------------------------------")

# Multi params Demo

def print_loc_1(*locations):
    print (locations, type(locations))

def print_loc_2(loc1, loc2, *locations):
    print (locations, type(locations))

print_loc_1("Hyderabad", "Mumbai", "Chennain", "Bangalore")
print ("------------------------------------------------------------------")
print_loc_2("Hyderabad", "Mumbai", "Chennain", "Bangalore")
print ("------------------------------------------------------------------")


# Multi key value paris demo

def print_details_1(**details):
    print (details, type(details))

def print_details_2(name, company, **details):
    print (details, type(details))

print_details_1(name="Teja", location="Bangalore", Salary=10000, company="Mindtree")
print ("------------------------------------------------------------------")
print_details_2(name="Teja", location="Bangalore", Salary=10000, company="Mindtree")


# Multi params and key value paris
def print_loc_details(*locations, **details):
    print (locations, type(locations))
    print (details, type(details))

print_loc_details("Hyderabad", "Mumbai", "Chennain", "Bangalore", name="Teja", location="Bangalore", Salary=10000, company="Mindtree")







