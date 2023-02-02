'''
we use finally:   error handling

'''

def func():
  try: 
    i=[1,2,3,4,5]
    l=int(input("Enter the Index  "))
    print(i[l])
    return 1
  except:
      print("Error Occured index or value error")
      return 0
  finally:
      print("i'm always print when any condition is print")
a=func()
print(a)
      
      
      
'''
raising custom errors
raise keyword for custom error stop when error are coming then show
'''
    
d=int(input("Enter value between 5 to 10 "))

if (d<5 or d>10 ):
    raise ValueError("enter value between only 5 to 10")
    
    
'''
defining custom expection 

'''
    
    
    
    
    
    