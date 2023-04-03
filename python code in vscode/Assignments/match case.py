c= input("what you want\np:plus m:minus")

match c:
    case "p":
        a=int(input("Enter the 1st value : "))
        b=int(input("Enter the second Value: "))
        print("multiply of a and b is: ",a*b)
    case "m":
        a=int(input("Enter the 1st value : "))
        b=int(input("Enter the second Value: "))
        print("Value of a minus b is: ",a-b)

        