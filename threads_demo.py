
import threading
import time


class MyThread(threading.Thread):
    #This name paramter is not madatory
    def __init__(self,name):
        threading.Thread.__init__(self) # You have to call the super class init method or an error is thrown
        self.name = name

    def run(self):
        lock.acquire() # Comment this to run paralelly
        for i in range(10):
            
            time.sleep(0.2) # Sleeps for number of seconds
            print ("in %s %d \n" %(self.name, i))
        lock.release() # Comment this to run paralelly
            

lock = threading.Lock()

t1 = MyThread("t1") # Creating thread object
t1.start() # Staring Thread

t2 = MyThread("t2") # Create another thread object
t2.start() # Starting Thread

t1.join() # Joining threads to prevent exit of main program
t2.join() # Joining threads to prevent exit of main program

print ("Main program exit")
