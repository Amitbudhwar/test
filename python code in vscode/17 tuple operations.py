# we have method to convert the tuple using undirectly


a=(2,5,1,-5)
tem=list(a)
tem.append(5)       # add items
tem.pop(2)          # delete item
tem[2]=10        # add itme in index
a=tuple(tem)     # convert list in tuple after change
print(type(a),a)

# we concatenate the tuple 

b=(-1,-3,-2,-3)
c=a+b            # we concatenate the two tuples
print("a+b is ",type(c),c)

# we can aslo use count , index slicing 


d=c.count(-3)
print("count how many time are available : - ",d)
print("length of c tuple : ",len(c))                            # length of tuple
print(c)
e=c.index(-1)                                               # slicing start with 5 or end in 17 search 4 index in 5 ton17 range
print("accurance/ index of : 1 is :-  ",e)



