l=[1,10,-1,-5,10]
print(l)

print("append ")
l.append(12)                    # we add the some values using append in existing list
print(l)

print("sort ")
l.sort()                        # USING SORT WE use assending order
print(l)

print("sort reverse ")
l.sort(reverse=True)            # we use this for decending order
print(l)

print("reverse ")
l.reverse()                     # existing list in reverse order
print(l)

print("indexing ")
print(l.index(-1))              # find the index (place) in list

print("count ")
print(l.count(10))   
# find the value in list how many time he come in list
print("copy ")
m=l.copy()                       # using copy we copy the list  in another 
print(m)

print("k is the reference of l")
k=l
k[0]=0
print(k)
print(l)

l.insert(2, 14)                     # we insert the value in any index 2 is the index and 14 is the value
print(l)

a=[100,900,500]
l.extend(a)                      # we merge the list inn existing list using extended
print(l)

# second method to concatinating the list

c= a + m                            # we can also this method to merge two eexisting lists
print(c)
















