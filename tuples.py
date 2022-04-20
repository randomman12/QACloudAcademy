#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Tuples"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Create an empty TUPLE
print ("CODE1")
EmptyTuple = ()
print(EmptyTuple)

#CODE2: Create TUPLE with 1 item
print("CODE2")
SingleTuple = (1,)
print(SingleTuple)

#CODE3: Create TUPLE with multiple items of the same type
print("CODE3")
MultiTuple1 = (1,2,3,4)
print(MultiTuple1)

#CODE4: Create TUPLE with multiple items of different types
print("CODE4")
MultiTuple2 = (1,"apple",4,"banana")
print(MultiTuple2)
#CODE5: Iterate over TUPLE with multiple items
print("CODE5")
for x in MultiTuple2:
    print (x)
#CODE6: Search in TUPLE
print("CODE6")

if MultiTuple2.index("apple") == True:
    print("present")
else: print("negative")

#CODE7: Retrieve item from TUPLE
print("CODE7")
print(MultiTuple2[2])
#CODE8: Attempt to change immutable TUPLE
print("CODE8")
try:
    MultiTuple2[0] = "not possible!"
except:
    print("Tuples are immutable!!")
print()
