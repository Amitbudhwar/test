with open('seek.txt','r') as f:
    print(type(f))
    
    f.seek(10)          # skip the first characters
    print("how many character is seek/skip: ",f.tell())     # current position where this read the character
    data=f.read()      
    print(data)
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    