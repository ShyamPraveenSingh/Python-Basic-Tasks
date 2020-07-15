#Program to open Calculator directly from the python program

#import the subprocess module
import subprocess


print('Enter any key to open calculator: ')
x = input()


#Opening the calculator (in Linux)
subprocess.Popen('/usr/bin/gnome-calculator')


#Opening the calculator (in Windows)
subprocess.Popen('C:\\Windows\\System32\\calc.exe')



