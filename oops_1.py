class Promit:
    def set_name(self, name):
        self.name = name    #name is an attribute of class promit that can be accessed
    def get_name(self): #self is a default parameter that is passed, that is used to signify the object passed with self
        return self.name
prom1 = Promit()    #how to create an object in class
prom1.set_name("Rahul")
print(prom1.name)
print(prom1.get_name()) #same output, name is an attribute now, self.<attr>=val