# # Write a program to print your name
Name=input("Enter your name :- ")
print("My name is",Name)


# # Write a program for a single lline and multiline comment

#  # is used to single line comment 
'''1. comment , escape sequence and print.py
 This comment is multiline comment

# '''

#  define the variable diff. data type int,boolean,string,float,char,double and print on the console

a=1
print("This is integer data type",type(a))

b=True
print("This is boolean data type",type(b))

c="Amit"
print("This is character data type",type(c))

d=34.56
print("Float Data type ",type(d))

e=chr(90)
print(e,type(e))



# local and global variable same name in one programe


total=0              #globale variable outside the function
def sum(x,y):
    total=x+y       # this is local variable inside the function
    print("I'M inside the function so im local variable",total)     # this is use for local variable print
    return total
sum(10, 3)           # local variable value
print("im outside the function so im global variable",total)    # this use for global variable print



