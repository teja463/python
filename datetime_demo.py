from datetime import datetime

print (datetime.now())


print ("Formated Date and Time: ", datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
print ("Formated Date and Time: ", datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
