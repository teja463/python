
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        time.sleep(2)
        end = time.time()
        print ("calc_sqr took %s milliseconds" % (str( (end - start) * 1000)))
        return ret
    return wrapper

        
            
@time_it
def calc_sqr(max_num):
    
    sqr_list = [num ** 2 for num in range(max_num+1)]
    
    return sqr_list
@time_it
def calc_cube(max_num):
    cube_list = [num ** 3 for num in range( max_num + 1)]
    return cube_list

print (calc_sqr(5))

print (calc_cube(5))
