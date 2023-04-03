# write a program print "Radhaswami"  10 time using for loop
print("Print same character 10 time")
for i in  range(10):
    print('RadhaSwami')
    
    
# Write a program to print 1 to 5 numbers using while loop
print("1 to 5 counting")
a=1
while (a<=5):
    print(a)
    a+=1
    
print("odd or even ")
print("even numbers 10 to 20 ")

for w in range(10,20):
     
    while w%2==0:
         print(w)   
         w+=1
    


print("odd numbers")
for b in range(10):
    if (b%2!=0):
        print(b)
        b+=1    


# find the largest numbers 
print("find greater number")
c=20
d=122
e=12
if c>d and c>e :
    print("c is greater")
elif d>e :
    
    print("d is greater ")

else:
    print("e is  greater")



# using match case / switch / find even and odd value 
x=int(input("Enter Number check number is even or odd:  "))
match x:
    
    # case _ if x<34:
    #     print("fail")
    # case _ if x>=34:
    #     print("pass")
    case _  if x%2==0:
      print("EVEN")
    case _ if x%2!=0:
        print("odd")
     
    
p=input("enter m and f \n m define MALE and \n f define FEMALE:  ")

match p:
    case 'm':
        print("male")
    case 'f':
        print("Female")
    case _ :
        print("other")

