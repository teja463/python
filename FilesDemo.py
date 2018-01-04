import os

pwd = os.getcwd()
files_dir = pwd + "/Files"
if (os.access(files_dir,os.F_OK)):
    print ("Directory exists no need to create it")
else:
    os.mkdir(files_dir)
    print ("Files directory created")
    
fname = pwd + "/Files/sample.txt"

# Write mode
fhandle = open(fname,"w")

fhandle.write("Line 1 \n")
fhandle.write("Line 2 \n")
fhandle.write("Line 3 \n")

fhandle.close()

# Append mode
fhandle = open(fname,"a")

fhandle.write("Line 4 \n")
fhandle.write("Line 5 \n")
fhandle.write("Line 6 \n")

fhandle.close()

# Read mode
fhandle = open(fname)

contents = fhandle.read(10)
print ("contents 1 ->", contents)

contents = fhandle.read(10)
print ("contents 2 ->", contents)

fhandle.seek(0)

contents = fhandle.readline()
print("contents 1:", contents)

contents = fhandle.readline()
print("contents 2:", contents)

contents = fhandle.readline(5) # Reads just 5 characters in that line
print("contents 3:", contents)


fhandle.seek(0)

all_lines = fhandle.readlines()
print (all_lines, type(all_lines))

for line in all_lines:
    print (line)

fhandle.close()
