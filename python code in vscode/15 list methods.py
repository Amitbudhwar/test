l=[1,2,4,10,-1,-5,10]
print(l)

l.append(12)                    # we add the some values using append in existing list
print(l)

l.sort()                        # USING SORT WE use assending order
print(l)

l.sort(reverse=True)            # we use this for decending order
print(l)

l.reverse()                     # existing list in reverse order
print(l)

print(l.index(10))              # find the index (place) in list

print(l.count(10))              # find the value in list how many time he come in list

m=l.copy()                       # using copy we copy the list  in another 
print(m)

l.insert(2, 14)                     # we insert the value in any index
print(l)

a=[100,900,500]
l.extend(a)                      # we merge the list inn existing list using extended
print(l)

# second method to concatinating the list

c= a + m                            # we can also this method to merge two eexisting lists
print(c)
















