#!python#
#Display all the files in the current directory and delete it

import os


#Display the list of files to be deleted
for filename in os.listdir():
    if filename.endswith('.py'): #.py extension can be changed to anything you want
        print('* ', filename)
        
print()
print('Do you want to delete all the following files permanently? (y/n): ')
response = input()


if response == 'y' or 'Y':
    for filename in os.listdir():
        if filename.endswith('.py'): #.py extension can be changed to anything you want
            os.unlink(filename)    
