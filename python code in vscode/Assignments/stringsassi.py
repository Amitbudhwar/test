# concatenate two strings

a='Amit '
b='Budhwar'
print(a+b)

# diff way create strings

a=''' 'RadhaSwami' "Budhwar" '''
c='''RAdHASWAMI'''
print("Different type of strings \n",a+c)


# find length of strings

print("Length of a ",len(a))
print("Length of b ",len(b))
print("Length of c ",len(c))

#replace character with replace()

d=c.replace('A', 'a')
print(d)

# string slicing
e='Amit'
print(e[2:4])


# split()

f='RadhaSwami ''RadhaSwami '"RadhaSwami"
g=f.split()
print(g)


#swapcase()   it convert uper case to lower and lower to uper
h='rADHAsWAMI'
i=h.swapcase()
print(i)

# isupper()    convert upper case
j='radhaswami'
k=j.upper()
print(k)
#lower()    converet lower case
l='RADHASwami'
k=l.lower()
print(k)

# convert type of integer to string type
m=1
print("this is integer :",m,type(m))
#convert integer type to strings
con_m = str(m)
print("convert integer to strings only type : ", con_m , type(con_m))


# search index in strings
n='RadhaSwami ji'
print(n.index('ji'))






