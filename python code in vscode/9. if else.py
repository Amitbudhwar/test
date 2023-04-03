''' 
if 
if-else
if-else-elif
nested if  -else-elif

conditional operator

< less, > , <= ,>= , == means equality check , != means not equal to
'''
# space is indentation

# a=int(input("Enter the Number :"))
a = 25
if a > 15:
    print("Hi")
if a <= 30:
    print("Hello")
else:
    print("Know Program")
    
# Find the time 


# for extra knowledge 
import time
tcheck=time.strftime('%H:%M:%S')
print("Time is :- ", tcheck)


# Write a programe to find the person give voote or not
print("Check you Give the vote or note")
a=int(input("Enter your age :- "))

if a>=18:
    print("You Give the Vote")
else:
    print("Try after one year")


# Check number the given number is odd or even

b=int(input("Enter the number check odd or even:- "))
if b%2==0:
    print("Number is EVEN ")
else:
    print("Number is odd")


# calculate the electric bill

''' question
first 100 units            no charge
101 units to 200 units     5rs. per unit
201 units to 500 units     10rs. perunits
'''

a=int(input("Enter you units : "))

if a<=100:
    print("NO Charge")
elif a>100 and a<=200:
    print("Charge is : ",(a-100)*5)
elif a>200 and a<=500:
    print("Charge is : ",(a-100)*5)
    

    


