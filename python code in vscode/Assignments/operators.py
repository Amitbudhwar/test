# write a programe for arithmetics operators (+,-,*,/)


a=int(input("Enter First number:- "))
b=int(input("Enter Second number:- "))

# + numbers

print(f"{a}+{b} =",a+b)
# multiply 
print(f"{a}*{b} =",a*b)
# minus
print(f"{a}-{b} =",a-b)
# Divide
print(f"{a}/{b} =",a/b)


# Increament and Decreaent Operators
print("Increament and decreament")
print("increament")
for c in range(10):
    print(c)
print("Decreament Start")
for d in range(10,0,-1):
    print(d)


# Write a prgrame find the numbers equal or not 

if (a==b):
    print("A is Equal to B")
else:
    print("A and B are Not Equal")
    

# Relational Operator (<,<==,>,>==)
print("Relational  operators")
print(a<b)
if a<b:
    print("a is less then b")
else:
    print("B is greater then A")
if a<=b:
    print("A is less then or equal to b")
else:
    print("B is Greator then A")

print("short methods")
# we can also wite a sort program to print relational operators like this

print("a is equal to b: ",a==b)
print("a is less then b: ",a<b)
print("a is less orequal to b: ",a<=b)
print("a is grater b: ",a>b)
print("a is greater or equal to b: ",a>=b)







