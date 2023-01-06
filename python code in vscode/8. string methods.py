# Strings are immutable (not change ) in plcae time. 

# Python provides a set of built in methods that we can use to alter and modify the strings.

# UPPER()      It converts a strings to upper case

a="Amit"
print(len(a))
print(a.upper())


# Lower()  It convert a strings in lower case.


a="AMiT"
print(a.lower())


# rstrip()   this remove any trailing character

a="AmIt!!!!!"
print(a.rstrip("!"))


# replace()replace all occurance of a string with another strings.a

a="AMiT"
print(a.replace("AMiT", "Budhwar"))


# split()   this method split the given string at the specified instance and return the 
# seprated strings as list items.

a="AMiT Budhwar"
print(a.split(" "))


# capatilize()  trun only the firest character of the string to upercase and rest other character in lower case

a="AMiT Budhwar"
print(a.capitalize())


# center() align the string to the center as per the paremeter given by the user.a


a="AMiT Budhwar"
print(a.center(50))

# count() return the number of items the given value has occured within the given strings.

a="AMiT Budhwar"
print(a.count(a))


# find() , index() , isalnum() , isalpha() , islower() , isprintable() , isspace() , istitle()  , swapcase()
# title() 1st all character are capital



