count = 100
rating = 4.34
is_published = True
course_name = "Python Programming"
ap = None


description = """
Hello
This is the description
"""

first = "teja"
last = "ponnuru"

full = f"{first} {last} {len(first)} {2+2}"
print(full)

# If block
temperature = 35

if (temperature > 30):
    print('drink water')
elif temperature > 20:
    print('dont drink water')
else:
    print('its cold')

# Ternary operator
age = 19
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# logical operators (and, or, not)
high_income = True
good_credit = True
student = False

if high_income and good_credit and not student:
    print("Eligible for creditcard")
else:
    print("Not eligible")

# For Loops
for number in range(3,8):
    print(number)

# While

number = 100
while number> 0:
    print(number)
    number = number//2

# Iterables
for x in range(2):
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

# functions

def add(a,b):
    return a + b

print(add(2,40))