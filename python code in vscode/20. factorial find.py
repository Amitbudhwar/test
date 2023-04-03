'''
factorial 7 is  7 * 6 * 5 * 4 * 3 * 2 * 1
factorial 6 is   6 * 5 * 4 * 3 * 2 * 1
........................................


factorial(n) = n * factorial (n-1) 



'''
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
a=int(input("Enter the factorial number :- "))    
print(factorial(a))

# we enter the value of a like 4 
# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * 1
        



