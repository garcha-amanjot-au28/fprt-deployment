# from oops import Animal # imported Class named Animal from oops.py
from abc import ABC, abstractmethod
#By defining an abstract base class, you can define a common Application Program Interface(API) 
# for a set of subclasses.
class Animal(ABC):
    # @abstractmethod
    def move(self):
        pass

    name = "Animal Name"
    is_alive = True
    
    def __init__(self,name, is_alive):
        self.__numberoflegs = 4
        self.name = name
        self.is_alive = is_alive
    def legs(self):
        print("Number of Legs: {}".format(self.__numberoflegs) )

    def setnumberoflegs(self,number):
        self.__numberoflegs= number

    def Animal_name(self):
        print("Animal name is :", self.name)
    
    
class humans(Animal):
    # def __init__(self,name,is_alive):
    #     Animal.__init__(self,"name",True)

    def move(self):
        print("I can walk and run")
    
class snake(humans):
    
    def move(self):
        print("i can crawl")

R = humans("Human",True)
R.move()
R = snake("Snake",True)
R.move()


# Principle#3 : Encapsulation Encapsulation is the method of keeping 
# all the state, variables, and methods private unless declared to be public.

Animal_name = Animal("Dog","is alive")

#Here when we try to change the number of legs , it does not change in aoutput as we used double __ 
#to make it a private attribute
Animal_name.__numberoflegs = 5 
Animal_name.legs()
#we can only change number of legs by using the setter function 
Animal_name.setnumberoflegs(5)
Animal_name.legs()


#Both Animal and Dog are examples of Class
class Dog(Animal): #Example of Single Inheritance 
    def __init__(self,Name,Breed):
        self.Breed= Breed
        self.Name = Name
        super().__init__("Dog",True)
    def Name_Breed(self):
        print("Name of Dog is :",self.Name)
        print("Breed name is :",self.Breed)
# Princeple#1 : Abstraction is the principle of hiding implementation of the class away 
# from anyting outside the class. Like you can see in the above example.


class Size:
    def __init__(self,Size):
        self.Size = Size

    def Actual_Size(self):
        print("Size of this Breed is ", self.Size)


class Breed(Dog,Size):#Example of Multiple Inheritance and also Multilevel Inheritance 
    def __init__(self,Colour):
        self.Colour = Colour
        # self.Name = Name 
        Dog.__init__(self,"Rodger",Breed)
        # Animal.__init__(self,"Dog",True)
        Size.__init__(self,Size)
       
        
    def Colour_name(self):
        print("Colour of ",self.Name," is ",self.Colour)
    def Actual_Size(self):
        print("Size of this breed is big")



#Below are all examples of objects
Rodger = Dog("Rodger","Pamerian") #created an object of class dog
Rodger.Animal_name()
Rodger.Name_Breed()

# As you can see in the above example the name " Rodger" is not accessible outside.

Rodger = Breed( "White")
Rodger.Colour_name()
Rodger.Animal_name()
Rodger.Actual_Size()
# Principle 4 : Polymorphism is a way of interfacing with objects and receiving different forms or results.
# Here Actual_Size returns 2 different results 
Rodger = Size("Small")
Rodger.Actual_Size()
