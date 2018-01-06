# Ans 1
monty_python = "Monty Python's Flying Circus".replace('y','i')
print ("Ans 1------------------------------------")
print (monty_python )

# Ans 2
sea_shells = "Sea shells on the sea shore"
print ("Ans 2------------------------------------")
print (sea_shells.count('s'))

# Ans 3
splits = "Monty Python's Flying Circus".split()
print ("Ans 3------------------------------------")
print (splits, type(splits))

# Ans 4
writing = "I am writing the python code"
splits2 = writing.split(' ')
print ("Ans 4------------------------------------")
print (splits2)

# Ans 5
print ("Ans 5------------------------------------")
in_str = input("Enter a string: ")

print (in_str[::-1])

# Ans 6
print ("Ans 6------------------------------------")
in_str2 = input("Enter a String: ")


while(not in_str2):
    in_str2 = input("Enter a String for Ans 6: ")

print (in_str2)

# Ans 7
print ("Ans 7------------------------------------")
ans_seven = writing.split(' ')
l = 0
while(l<len(ans_seven)):
    print (l)
    l += 1

for ele in ans_seven:
    print (ele)

# Ans 8
print ("Ans 8------------------------------------")
ans_8 = "Monty Python's Flying Circus".split()

for a in ans_8:
    print (a, len(a))

# Ans 9
print ("Ans 9------------------------------------")
in_num = int(input("Enter a number: "))
sq_list = [num ** 2 for num in range(1,in_num+1)]
print (sq_list)

# Ans 10
print ("Ans 10------------------------------------")
loc_list = ["Hyderabad", "Noida", "Bangalore", "Nellore"]

for loc in loc_list:
    if loc.startswith("N"):
        print (loc , "->", len(loc))

# Ans 11
print ("Ans 11------------------------------------")

numbers = list(range(1,11))
numbers.append(11)
numbers.insert(0,0)
print (sorted(numbers,reverse=True))
print ("count", len(numbers))
print ("max index", len(numbers)-1)

for number in numbers:
    print (number)

n = 0
while (n <len(numbers)):
    print( numbers[n] )
    n += 1

print (numbers[::2])

# Ans 12
print ("Ans 12------------------------------------")
software_det = {"java":1.8,"python":3.6,"html":5}

print (software_det.keys())
print (software_det.values())

for key in software_det:
    print ("The Software %s has been installed with the version %s" %(key, software_det[key]))



# Ans 17
print ("Ans 17------------------------------------")
import re

emails = ["teja_463@gmail.com", "test@google.com"]
for email in emails:
    if(re.search("^[a-zA-Z]{4}[._]\d{3}@\w.\w",email)):
        print ("Username: ",email.split("@").pop(0))
        print ("Email: ",email.split("@").pop(1))


# Ans 19
print ("Ans 19------------------------------------")
string = "This is a simple string with three four and five letter words"
print (re.findall(r"\b\w{3,5}\b", string))

# Ans 20
print ("Ans 20------------------------------------")
str_all = re.sub("\s","", string)
print (str_all)

# Ans 21
print ("Ans 21------------------------------------")
url_str = "http://google.com http://yahooo.com http://test.com"
url_all = re.findall("http://\w+.\w+",url_str)
print (url_all)
