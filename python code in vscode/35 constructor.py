class person:
    def __init__(self,n,o):         #object
        print("RadhaSwami")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a  {self.occ}")


a=person("Amit","Developeri")
b=person("Deepak","Bank Manager")
c=person("Hardeep","Digital Manager")
a.info()
b.info()
c.info()

# a.info()



