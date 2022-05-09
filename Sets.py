#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Sets"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Create an empty SET
set1 = {""}
print (set1)
#CODE2: Create SET with 1 item
set2 = {"banana"}
print (set2)
#CODE3: Create SET with multiple items of the same type
set3 = {"banana", "apple", "strawberry", "peach"}
print (set3)
#CODE4: Create SET with multiple items of different types
set4 = {"2", "square", "4"}
print (set4)
#CODE5: Iterate over SET with multiple items
for i in set4:
    print (i)

#CODE6: Search in SET
print ("banana" in set3)
print ("2" in set4)

#CODE7: Attempt to retrieve item from SET
try:
    item0 = set4[0]
    item1 = set4[1]
except:
    print("Sets don't support indexing")
#CODE8: Add new unique item to SET
set3.add("chicken")
print(set3)

#CODE9: Add new non-unique item to SET
set3.add("chicken")
print(set3)

#CODE10: Remove item from SET
set3.remove("strawberry")
print(set3)
