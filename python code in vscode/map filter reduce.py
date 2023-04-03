def cube(x):
    return x*x*x
print(cube(5))


l=[1,2,3,4,5]
nl=list(map(cube, l))
print(nl)