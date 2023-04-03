class person:
    name=input("Enter your name: ")                     
    occupation=input("Enter your occupation: ")
    networth="50000"
    age=23
    def info(self):         # self woo object jiske (uper ye method call ) liye call kiya jaa rha  h
        print(f"{self.name} complete {self.occupation} and its age is {self.age}")
    
    
a=person()
b=person()
c=person()
d=person()
a.age=22
b.name="Deepak"
b.occupation="Bank Manager"

c.name="Dinesh"
c.occupation="H.O.D"

d.name="Hardeep"
d.occupation="Digital marketing HOD"


a.info()
b.info()
c.info()
d.info()
