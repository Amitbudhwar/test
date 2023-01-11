# uodate

ep1={100:200,34:300}
ep2={110:150,30:350}
ep1.update(ep2)
print(ep1)
ep1.clear()                                                     #use clear() to clear the all values
print("use clear() to clear the all values",ep1)
empt={}                                                         #empty dictionary
print("empty dictionary :- ",type(empt),empt)
a={1:10,2:20,3:30,4:40,5:50,6:60}
a.pop(1)                                                        #remove the key and value
print("remove the key and value ",a)
a.popitem()                                                     #remove the last key value                                    
print("remove the last key value ",a)
# del a                                                           # delete the dictionary
del a[2]
print(a)

