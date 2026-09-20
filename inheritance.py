# class and object Inheritace


class vahicle:
    def fuel_tupe(self):
        print("This vahicle uses discel & petrol")
    def print_name(self):
        print("My name is preethi")  


class Electricity(vahicle):
    def fuel_tupe(self):
        print("This vahicle uses battery") 
v = vahicle()
aadi = Electricity()
v.fuel_tupe()
print
aadi.fuel_tupe()
aadi.print_name()


# polymorphism overloading [diff class same method]


class Dog:

    def speak(self):
        print("Dog is barking")
class Cat:
    def speak(self):
        print("Cat is meow")

d1 = Dog() 
c1 = Cat()
d1.speak()
c1.speak()


class calculater:

   def add(self,a,b=0,c=0):
    return a + b + c
calc = calculater()
print("Adding 2 number (10+20):",calc.add(10,20))
print("Adding 3 number (10+20+30):",calc.add(10,20,30))


# Encapsulation  [hide data]

class  my_phone:
    def __init__(self,serialno,brand):
        self.brand = brand
        self.__serial__no = serialno

    def get_serialno(self):
        return self.__serial__no    
    
    
p1 = my_phone('x90123455','vivo')
print("secure serialno:",p1.get_serialno())

# class ,object
class Book:
  
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):  
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price: Rs.",self.price)

my_book = Book("Python Basics", "preethi", 299)  
my_book2 = Book("java Basics", "sam", 499)
print("--- Book Details ---")
my_book.display_info()   
print(my_book.title)

my_book2.display_info()