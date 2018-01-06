# Generators

def loc_generator():
    yield "Hyderabad"
    yield "Bangalore"
    yield "Chennai"

loc = loc_generator()

try:
    print ("one: ",loc.__next__())
    print ("two: ",loc.__next__())
    print ("Three: ",loc.__next__())
    
except StopIteration as si:
    print (si)



def yrange(max_num,step=1):
    num = step
    while(num<max_num):
        yield num
        num += step

y = yrange(10)

print (list(y))
