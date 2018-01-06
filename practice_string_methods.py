string = "Teja"

print (string.replace("T","H"))
print (string)

sample = "Teja" * 5

print (sample, type(sample))
sample_list = ["0"]*5
print (sample_list)


# number = int(input("Enter a number: "))
number = 22
print (number)


if number <100:
    print ("Less than", "hundred")
elif number >100 and number <200:
    print ("In between ", 100 , "and ", 200)
else:
    print ("Greater than 200")

for i in range (6):
    print (i)
else:
    print ("for loop completed successfully..")

str_list = "Hello how are you".split()

print (str_list)
print (",".join(str_list))

for s in str_list[::-1]:
    print (s)

list_mul = [i **2 for i in range (6) if i % 2 ==0 ]
print (list_mul)

# dictionary comprehension

locations = ["Hyderabad", "Bangalore", "Chennai", "Goa", "Mumbai", "Pune"]

loc_len = {l:len(l) for l in locations if l.endswith('e')}
print (loc_len)
