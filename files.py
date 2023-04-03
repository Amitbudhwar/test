<<<<<<< HEAD
# f=open('sample.txt','r')
# data=f.read()
# print(data)
# f.close()

# f=open('amit.txt','w')
# f.write("budhwar python 1")
# f.close()

# with open('amit.txt') as f:
#     a=f.read()
#     print(a)
    
    
# with open('amit.txt','w') as f:
#         a=f.write('my name is amit i learn python')
#         print(a)

for i in range(2,7):
    with open(f"table{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}\n")

        
=======
# f=open('sample.txt','r')
# data=f.read()
# print(data)
# f.close()

# f=open('amit.txt','w')
# f.write("budhwar python 1")
# f.close()

# with open('amit.txt') as f:
#     a=f.read()
#     print(a)
    
    
# with open('amit.txt','w') as f:
#         a=f.write('my name is amit i learn python')
#         print(a)

for i in range(2,7):
    with open(f"table{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}\n")

        
>>>>>>> f247df1 (python files)
