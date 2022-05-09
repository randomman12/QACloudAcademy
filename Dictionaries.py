#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Dictionaries"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Create an empty DICTIONARY
dict1 = {}
print (dict1)

#CODE2: Create DICTIONARY with 1 key-value pair
dict2 = {"brand": "ford"}
print (dict2)
#CODE3: Create DICTIONARY with multiple key-value pairs
dict3 = {"brand": "ford", "model": "focus"}
print(dict3)

#CODE4: Create DICTIONARY with multiple and nested key-value pairs
dict4 = {"brand": "ford", "model": "focus"}
print(dict4)
#CODE5: Iterate over DICTIONARY with multiple and nested key-value pairs
dict5 = {"brand": "ford", "model": "focus", "data": {"val1": 1, "val2": 2}}
#CODE6: Search key in DICTIONARY


#CODE7: Retrieve value from DICTIONARY by key

#CODE8: Change existing value in DICTIONARY

#CODE9: Add new key-value pair to DICTIONARY

#CODE10: Pop existing key-value pair from DICTIONARY

#CODE11: Pop non-existing key-value pair from DICTIONARY
