#public modifier
class Class1:
    def __init__(self):
        self.pub_attribute = None

    def pub_method(self):
        print(self.pub_attribute)

#private modifier
class Class2:
    def __init__(self):
        self.__priv_attribute = None

    def __priv_method(self):
        print(self.__priv_attribute)
    
    def __private_method2(self):
        print(self.__priv_attribute)

#protected modifier
class Class3:
    def __init__(self):
        self._prot_attribute = None

    def _prot_method(self):
        print(self._prot_attribute)
#whenever defining a class and within a method not passing anything 
#need to pass self
#when a class inherits the properties of another class, it is called a subclass
#subclass(Child class) will be able to access the protected modifiers of the SuperClass(Parent class)
class Class4(Class3):
    def __init__(self):
        super().__init__()
        self._prot_attribute = 1

    def _prot_method(self):
        print(self._prot_attribute)

#Class4()._prot_method()


