import os

# .environ method gives the environment varialbes in the form of dictionary
env_variables = os.environ
print (env_variables, type(env_variables))


# Iterate and print the variables one by one
#for key, val in env_variables.items():
#    print (key, "->", val)

# Get only the ones you need
print ("Username", env_variables['USERNAME'])

"""for root, directories, fnames in os.walk(os.getcwd()):
    print ("Dir path", root)
    print ("List of directories at root", directories)
    print ("List of files", fnames)
    print ("***********************************************")
"""
dir_name = os.getcwd()

print (os.path.isdir(dir_name))
print (os.path.basename(dir_name))
print (os.path.dirname(dir_name))
