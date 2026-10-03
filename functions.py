student marksheet
def adding_numbers (a,b,c):
    return a + b + c
print (adding_numbers (100, 60, 70))


def student_mark(*args,**kwargs):
    print("\n student_name:")
    for i in args:
        print(f"{i}")
    print(f"marks: {kwargs.get('python')}")

student_mark("preethi","ram",python=100,java=80)

def print_student_detail(name,marks):
    print(f"student_name {name},student_mark {marks}")

print_student_detail("preethi",100)
  
def calculate_total(mark_list):
    total = sum(mark_list)
    print(total)
mark = [100,60,70]
calculate_total(mark)



def student_mark(n):
    if n == 0:
        return
    student_mark

    print(f"Student {n} mark: {mark}")
student_mark(5)

def order_food(*args,**kwargs):
    print("\n Item ordered")
    for item in args:
        print(f"{item}")
    print(f"Delivery detail:sending to {kwargs.get('name')} at {kwargs.get('address')}")        
order_food("pizza","coke",name = "sam",address = "paris")
def greet():
    print("Hello Preethii")
greet()    
def greet(name):
    print("Hello",name)
greet("preethi")    
def greet(name,age):
    print("hello",name,"age is",age)
greet("preethi",19)    
def greet(a,b):
    return a + b
print(greet(10,20))    
def greet(name = "preethi"):
    print("hello",name)
greet()    
def greet(*args):
    calculate = 0
    for number in args:
        calculate = calculate + number
    print(calculate)    
greet(10,20,30)    
def student(**kwargs):
    print(kwargs)
student(name ="preethi",age =19 , course ="python")    
name = "preethi"
def greet(name,age):
    print(name,19)
greet("preethi")    
name = "preethy"
def greet():
    city = "paris"
    print(name)
    print(city)
greet()  
print(name)  
def add(*args):
    total = 0
    for number in args:
        total = total + number
    print(total)
add(10,20,30,40)        
def y(number):
    if number == 0:
        print("")
    else:
        print(number)
        y(number-1)
y(10)        

def factorial(n):
    if n ==0:
        print("")
    else:
        print(n)
        factorial(n-1)
factorial(5)  

number = int(input("Enter your number:"))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negtive number")
else:
    print("Zero") 

for i in range(10,0,-1):
    print(i)
numbers = [10,20,30,40,50]
total =   sum(numbers)
print ("sum = ", total)
numbers = (20.50,5,70,89,10,3,)
small= min(numbers)
print("smallest = ",small)
number = [10,3,4,5,5,3,10]
uni_value = list(set(number))
print(uni_value)
num = int(input("Enter your Number:"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial* i
print(factorial)    
number = [1,5,67,8,9,0]
number.reverse()
print(number)
set1 = {1,3,5,67,8,9,0,}
set2 = {3,5,6,8,0.4,98,77}
common = set1.intersection(set2)
print(common)
row = 5
for i in range(1,row+1):
    print("*" * i)
text = input("Enter a string: ")
count = 0
for ch in text: 
    if ch.upper() in "AEIOU": 
        count += 1
print("Number of vowels =", count)
def calculate (a,b):
    return (a+b)

print(calculate(10,20))
check = lambda n: "even" if n % 2 != 0 else "odd"
print(check(10))
print(check(9))
multiplay = lambda a,b: a*b
print(multiplay(5,4))
small = lambda a,b: a if a<b else b
print(small(0,3))
number = [3,8,12,17,20,25,30]
result = list(filter(lambda x: x >10 and x<25 ,number))
print(result)



class mobile:
    brand = "vivo"
    price = 10000
mobile1 = mobile()    
print(mobile1.brand)
print(mobile1.price)
class student:
    name = "preethi"
    age = 20
student1 = student()
print(student1.name)
print(student1.age)  
class student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

student1 = student("preethi", 19, "Coimbatore")
print(student1.name)
print(student1.age)
print(student1.city)

student2 = student("sam", 20, "Coimbatore")
print(student2.name)
print(student2.age)
print(student2.city)

student3 = student("Arun", 21, "Coimbatore")
print(student3.name)
print(student3.age)
print(student3.city)
class student:
    def greet(self):
        print("hloo preethi")
student1 = student()
student1.greet()        
class Book:
    def __init__(self,author,title,price):
        self.author = author
        self.title = title
        self.price = price
    def display_info(self):
        
        print("Author:",self.author)
        print("Title:",self.title)
        print("Price:",self.price)
book1 = Book("preethyy","Python",900)
book2 = Book("sam","java",899) 
# book1.display_info()  
book2.display_info()  
print(book2.author)  
class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
car1 = car("Toyota","Innova") 

car1.display_info()
class Mom():
    def phone(self):
        print("Moms phone")
class Dad:
    def Sweet(self):
        print("Dad's sweet")        
class Son(Mom,Dad):
    def tab(self):
        print("Son's tab")
sam=Son()
sam.tab()
sam.phone()
sam.Sweet()

class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
class Dog(Animal):
    pass
dog1 = Dog()
dog1.eat()
dog1.sleep()
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
class Student(Person):
    pass
student1 = Student("preethi",19)
student1.display_info()

class Vahicle:
    def start(self):
        print("Vahicle is starting")
class Car(Vahicle):
    pass
car1 = Car()
car1.start()

class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog:
    def sound(Animal):
        print("Dog barks")
class Bird:
    def sound(Animal):
        print("Bird sing")    
dog1 = Dog()
bird1 = Bird()
a1=Animal()
dog1.sound()
bird1.sound()
a1.sound()

class Add:
    def calculate(self ,a=10,b=20):
        return a+b
class multiplay:
    def calculate(self,a= 10,b=20):
        return a*b
a1=Add()

m1=multiplay
print(a1.calculate())
print(m1.calculate())

class Animal:
    def sound(self):
        print("animal is sleep")

class Dog(Animal):
    def sound(self):
        print("dog is bark")
class Cat(Animal):
   def sound(self):
        print("cat is meow")
a1=Animal()
a1.sound()
d1=Dog()
d1.sound()
c1=Cat()
c1.sound()

class calculator():
    def operations(self):
        pass
class Add(calculator):
      def operations(self ,a=10,b=5 ):
        print(a+b)
class Multiplay(calculator):
    def operations(self,a=10,b=5):
        print(a*b)
a=Add()
m=Multiplay()
a.operations()
m.operations()                






