
# Execute this file from the command prompt
import sys

print ("Python version", sys.version)

print ("Command line arguments passed", sys.argv)

for i in range(1, len(sys.argv) ):
    print ("argument ",i, sys.argv[i]) 
