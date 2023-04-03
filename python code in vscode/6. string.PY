'''   

STRING
STRING
STRING



IN Python , anything that you enclose between single or double quotatioon marks is considered a string.
A string is essentially a sequence or array of textual data. String are used when working with unicode 
character



Double quatation   ""
Single Quatation    ''




'''


Name="Amit"
Sirname="Budhwar"
print('My Name is : ',Name + Sirname)

# single line and Multi line  

intro='''
My name is ,"Amit".I Learn Devop's.
We can use multi line using 3 single quatation and we also use 'single'
and "double quote" in multi and single line
'''
print(intro + Name + Sirname)



# Access Character
# Access Character
# Access Character
# Access Character
# [] using this we can accesss string using  this

print(Name[0])
print(Name[1])
print(Name[2])


# We can print all character using loop
# We can print all character using loop
# We can print all character using loop
print("using for loop we Print ALL character ")
for character in Name:
    print(character)

