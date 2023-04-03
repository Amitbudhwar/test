# a="ab"
# print(f"multi table of {a} is : ")

# try:
#     for i in range(1,11):
#      print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:                   # this line use for what is the error**** e ****define the error
# # #  # we print without** e **using****** expect: print("enter your message") ******
#     print(e)


try:
    b=int(input("Enter integer value 'dont enter int value for value error see' "))
    c=[2,3]
    print(c[b])
except ValueError:
    print("enter only integer value ")
except IndexError:
    print("index error 'index error when we are not entered in the range '")    


