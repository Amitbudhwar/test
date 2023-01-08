# def average(a,b):
#     print("the average is :- ",(a+b)/2)
# average(4, 6)

# def name(fname,mname="amit",bname="deepak"):
#     print("Hello ",fname,mname,bname)
# name("JagjitSingh", "Deepak","Amit")                # overwrite 
    
# tuple

# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("Average is : ",sum/len(numbers))
# average(2,10)


# dict



def name(**name):
    print(type(name))
    print("Hello" , name["fname"], name["bname"])
    
    
    
name(fname="Jagjit",bname="Deepak")

















