# Ans 1
monty_python = "Monty Python's Flying Circus".replace('y','i')
print ("Ans 1",monty_python )

# Ans 2
sea_shells = "Sea shells on the sea shore"
print ("Ans 2",sea_shells.count('s'))

# Ans 3
splits = "Monty Python's Flying Circus".split()
print ("Ans 3", splits, type(splits))

# Ans 4
writing = "I am writing the python code"
splits2 = writing.split(' ')
print ("Ans 4", splits2)

# Ans 5
in_str = input("Enter a string: ")
print ("Ans 5",in_str[::-1])

# Ans 6
in_str2 = input("Enter a String: ")

while(not in_str2):
    in_str2 = input("Enter a String for Ans 6: ")

print ("Ans 6", in_str2)

# Ans 7
ans_seven = writing.split(' ')
l = 0
while(l<len(ans_seven)):
    print ("Ans 7",l)
    l += 1

for ele in ans_seven:
    print ("Ans 7",ele)

# Ans 8
ans_8 = "Monty Python's Flying Circus".split()

for a in ans_8:
    print ("Ans 8", a, len(a))
