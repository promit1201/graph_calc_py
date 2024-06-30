class Parent:
    def __init__(self):
        print("This is the parent class")
        self.sup_attribute = True
class Child(Parent):
    def __init__(self):
        print("This is the child class")
        super().__init__()
        print(self.sup_attribute)
child1 = Child()
# This is the child class
# This is the parent class
# 'super()' is a method that refers to the parent class

#there are two types of inheritance, single and multiple
#single inheritance refers to one class attributes inherited by another class
#multiple inheritance refers to more than one class attributes inherited by another class


#multi level inheritance refers to more number of classes inheriting from one another at levels 
#a->b->c(multi level inheritance)
#a=base class(grandparent class)
#b=parent class(intermediary class)
#c=child class(derived class)


#hierarchial inheritance refers to one base class from which other classes(plural) inherit directly, derived

#hybrid inheritance=> class A, class B, class C(A,B), class D(C)
#hybrid means any combination of types of classes or reverse of inheritance