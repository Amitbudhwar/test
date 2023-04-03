'''
it appear right after the defntion of a function method , class,or modules.
.__doc__     using this we can access the Doc String

*****doc string write below the function name and write above the function body*****
*****pep -8 it stand for python enhancement proposal*****

**** pep is a DOcument that describe the new feature proposed for  python and document like design and style
fot thhe community.******

**** Zen of  python *****
we see  type****   import this    ****
   


'''


# use doc string and find square root with function
def square(n):
    ''' this is doc string example in 3 dot'''
    print(n**2)
b=int(input("Enter Value for find the Square root :- "))
square(b)
print(square.__doc__)





