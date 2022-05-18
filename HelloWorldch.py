#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "HelloWorld"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))

print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Declare message variables
messg = 'Hey'
print (messg)
#CODE2: Use string concaternation then print to the console
messg = messg + ' stinky head'
print( messg)
#CODE3: Use string formatting and interpolation then print to the console
print ("%s %s" %('Hello', 'World'))
#CODE4: Uppercase the message vars before printing to the console:
print(messg.upper())
#CODE5: Create an array of words and then loop over array and determine string length of each word
arr = ['chicken',  'beef', 'lamb']
for i in arr:
    print (i, len(i))
