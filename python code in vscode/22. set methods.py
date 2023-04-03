


# union or intersection method


a={1,2,3,4}
b={4,5,6}
print("a and b is :- ",a,b)

#union

c=(a.union(b))
print("Union of a and b is:- ",c)

# intersaction 

d=a.intersection(b)
print("Intersection of a and b is:- ",d)

# symetric 

e=a.symmetric_difference(b)
print("Symetric diff :- ",e)


# update method

a.update(b)
print("Update method union :- ",a,b)

a.intersection_update(b)
print("Intersection_update method :- ",a,b)

# isdisjoint 
# both are same then FALSE otherwise TRUE

z={1,2,3,4,5,6}
x={1,2,3,4}
print("isdisjoint :- ",z.isdisjoint(x))

# issuperset   or issubset
# z k andr x ki sabhi values available h ya nhi
# opposite issuperset

print("issuperset :- ",z.issuperset(x))
print("issuperset :- ",z.issubset(x))

# add() and update or remove/ discard
# he add the variables
z.add(7)
print("we add the item using add():- ",z)
z.update(x)
print("combine the both variable :- ",z)
x.remove(1)
print("remove the item using remove() :- ",x)
x.discard(1)
print("Error not show when value not available in variable:- ",x)
w=x.pop()
print("Random value is remove usin pop():- ",x)
print("which value is pop/remove",w)

# del  is use we remove the variable it is a keyword i think

q={1,2}
print("After this q is deleted:- ",q)
del q
# print(q)    # uncomment he ine and run q is not define
s={1,2,3}
s.clear()
print("clear the items and print empty set:- ",s)









