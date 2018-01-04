import os


cur_dir = os.getcwd()
files_dir  = cur_dir+"/Files"
fname = files_dir+"/sample2.txt"

print (cur_dir)
print (os.access(files_dir, os.F_OK))
print (os.access(files_dir, os.X_OK))
print (os.path.isdir(files_dir))

fhandle = open(fname, "w")

fhandle.write("This is Line 1\n")
fhandle.write("This is Line 2\n")
fhandle.write("This is Line 3\n")

fhandle.close()

fhandle = open(fname, "a")

fhandle.write("Appending Line 4\n")
fhandle.write("Appending Line 5\n")
fhandle.write("Appending Line 6\n")

fhandle.close()



fhandle = open(fname,"r")
contents = fhandle.read(5)
print (contents)
contents = fhandle.read(5)
print (contents)

fhandle.seek(0)

contents = fhandle.readline()
print (contents)
contents = fhandle.readline(5)
print (contents)

fhandle.seek(0)
contents = fhandle.readlines()
print (type(contents))
for line in contents:
    print (line)
