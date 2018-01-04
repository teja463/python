import logging_module

def test_logging(statement):
    print (logging_module.deb)
    logging_module.debug(statement)
    logging_module.info(statement)
    return ("1","2","3")

a,b,c = test_logging("Hello")

if (a is None or b is None or c is None):
    print ("None")
else:
    print ("not None", a, b, c)


tup = [x ** 2  for x in range(1, 6) if (x ** 2) % 2 == 0 ]
print (tup.count(4))


even_lambda = lambda x: x%2 == 0
odd_lambda = lambda x: x%2 !=0

sample_list = [1,2,3,4,5,6,7,8,9,10]
print ("all elements", sample_list)

even_list = list(filter(even_lambda, sample_list))
odd_list = list(filter(odd_lambda, sample_list))
print ("even elements", even_list)
print ("odd elements", odd_list)

even_map =list(map(even_lambda, sample_list))
print("even map", even_map)


palind = lambda s: s==s[::-1]
s_list = ["radar", "teja", "malayalam", "pramod"]
palind_list = map(palind, s_list)
print (list(palind_list))
