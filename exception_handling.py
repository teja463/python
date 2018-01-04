# Example 1
try:
    num = 1/0
except:
    print ("Caught exception")

# Example 2 Generic Handling

try:
    num2 = 1/0
except Exception as e:
    print ("Handling in generic way")

# Normal Handling

try:
    num3 = 1/1 # change denominator 1 to 0 to generate ZeroDivisionError
    name = "Teja" # Remove this line to generate NameError
    print (name)
    print (name + 2)
except ZeroDivisionError:
    print ("Zero error occured")
except NameError as ne:
    print ("Name error due to not defined",ne)
except (ZeroDivisionError, NameError) as e:
    print ("Can catch bot the ex,ceptions")
except Exception as e:
    print ("Generic exception occured", e)
else:
    print ("This will be executed only when all statements are executed successfully")
finally:
    print ("Same as finallly in java")

# User defined exception

class InvalidEmailException(Exception):
    my_err_msg = "Use did not enter mindtree mail id -> "

try:
    mail_id = input("Enter mail id: ")
    if (mail_id.count("@") == 1 and mail_id.endswith("@mindtree.com")):
        print ("Valid mail id", mail_id)
    else:
        raise InvalidEmailException
except InvalidEmailException as ime:
    print (ime.my_err_msg, mail_id)
