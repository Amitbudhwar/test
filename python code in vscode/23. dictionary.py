'''
****dictionary is ordered . they store multiple colection ieteem in a single varible
key value pair that are seprated by commas, and enclose with curly bracket{} and value enclose in ""
changable
enclose with {} ****

dicname        give error when key not exist
dicname.get    not give error when key is not available in dictionay
dicname.keys()         print all values available in dictionary using for loop

 
'''
dic={
    1:"Amit",
    2:"Deepak",
    3:"Dinesh",
    4: "Prince"    
}
print(dic.get(1))

print("we print the all keys :- ",dic.keys())
print("we print the all values :- ",dic.values())

for key in dic.keys():          #iterate
    print(f"The values corresponding to the key {key} is :- ",dic[key])
    
for key,value in dic.items():
    print(f"The values corresponding to the key {key} and value is {value}")
    

