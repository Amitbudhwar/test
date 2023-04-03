def cube(x):
    return x*x*x
print(cube(5))

# Using map Functon
# Using map Functon
# Using map Functon
# Using map Functon

print("\nthis is map")
l=[1,2,2,3,4,5,10]
nl=list(map(cube, l))
print(nl)

# we can use this in lambda function we commint the def cube
print("\nwe use also a lambda function in map ")
l=[1,2,2,3,4,5,10]
nl=list(map(lambda d: d*d, l))
print(nl)


# filter
# filter
# filter
print("\nthis is filter")
def fil_fun(a):
    return a>4
s=list(filter(fil_fun,l))
print(s)


# reduce
# reduce
# reduce
print("\nREDUCE Function")

from functools import reduce
number=[2,3,5,2,6,2]
# def msum(x,y):
    # return x+y
sum1=reduce(lambda x,y:x+y,number)
print(sum1)









