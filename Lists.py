#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Lists"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Create an empty LIST
emptylist = [""]
print (emptylist)
#CODE2: Create LIST with 1 item
onelist = ["banana"]
print (onelist)

#CODE3: Create LIST with multiple items of the same type
multilist = ["banana", "apple", "pear"]
print(multilist)

#CODE4: Create LIST with multiple items of different types
diflist = ["1", "banana"]
print (diflist)
#CODE5: Iterate over LIST with multiple items
list = ["chicken", "beef", "bacon", "egg"]
for i in list:
    print(i)

#CODE6: Search in LIST
twolist = ["chicken", "beef", "bacon", "egg"]
print ("chicken" in twolist)

#CODE7: Retrieve item from LIST
item0 = twolist[0]
item1 = twolist[1]
#CODE8: Attempt to change mutable LIST
twolist[0] = "possible!"
#CODE9: Append to LIST
twolist.append("pork")
print (twolist)
