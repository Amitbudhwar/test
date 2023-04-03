# a=[]
# print(type(a))

# b=(1,2,3,4,5,6,7,8,9)
# # print(type(b))
# # print(len(b))
# # print(b[1:8])
# print(b[-8:-3])

# li=[i*i for i in range (4)]   # list comprehasion
# print(li)


# a=[1,2,3]
# # a[0]=4
# b=tuple(a)

# print(type(a))
# print(type(b))
# print(a)
# print(b)



# ab={1,2,3,4,5,2,6,7}
# # ab.remove(4)    # remove give error in set
# # ab.discard(8)   # discard not give error
# dc=ab.pop()
# # del dc
# ab.clear()
# print(ab)
# print(dc)
# bc={6,7,8,9,10}
# bc.update(ab)
# print(bc)







# di= {1:"amit",2:"deepak"}
# print(di[1])
# print(di.get(3)) # .get not through the error
# # print(di.keys())

# for keyy in di.keys():
#     print(f"hlo {keyy} is {di[keyy]}")





# a=input("Enter the table name")
# print(f"multiplication of {a} is ")
# try:
#     for i in range(11):
#      print(f"{a} X {i} = {int(a)*i}")
# try:
# h=int(input("enter the Index Number : "))

# if (h<2 or h>10 ):
#         raise ValueError("Chup RH ")
# g=[1,2,3,4,5,6]
# print(g[h])
    
# except Exception as e:
#     print(e)
# except ValueError:
#     print("Not Integer")
# except IndexError:
#     print("Enter Right Index")
# finally:
#  print("I'm Finally im Always Execute")




# a=2
# b=2
# print("A") if a>b else print("B") if a==b  else print("B")



# q=[1,2,3,4]
# w=(1,2,3,4)
# e={1,2,3,4}
# t={1:'a',2:'b',3:'v',4:'f',5:'e'}


# r=slice(1,3)
# print(q[r])
# print(w[r])
# # print(e[r]) # slicing not allowed in set
# print(type(t),t)
# # print(t[r])# slicing not allowed in dictionary





# class ai():
#     # name=input("Enter Your Name: ")
#     # occu=input("Enter Your occupation: ")
#     def __init__(self,n,o): #   __init__(self)  Default construction     __init__(self,n,o) perameter
#         self.name=n
#         self.occu=o
#     def info(self):
#         print(f"{self.name} complete {self.occu}")
    
# a=ai(input(" 'Im the value of A'\n Enter Your name: "),input("Enter occupation: "))
# b=ai("Deepak","State Head")
# # b.name="Amit"
# # print(ab.name,"\n",ab.occu)   
# a.info()
# b.info()



# import calendar
# print(calendar.calendar(2023))


# import random
# print("Random Number Generator",random.randint(0,100000))




# a=['amit','deepak','dinesh']
# for ab in a:
#     print(ab)
#     for i in ab:
#          print(i)


# for i in range(2,11,2):
#     print(i)


# i=0
# while (i<11):
#     print(i)
#     i+=2

for i in range(11):
    # 
    if i == 8:
        print('skip the iteration')
        continue
    print(f'5*{i}','=', 5*i)
    # print(i)
        
    
    





