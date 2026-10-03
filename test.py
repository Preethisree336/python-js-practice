star = "*"
i = 1
while i <= 5:
    print(star * i)
    i+=1
    
star = "*"
i = 5
while i >= 1:
    print(star * i)
    i-=1

star = '*'
for i in range(1,6):
    print(star * i)
a = 0
b = 1
for i in range(10):
    print(a)
    c = a+b
    a=b 
    b=c

a = 0
b = 1
i = 0
while i < 10:
    print(a)
    c = a+b
    a=b
    b=c
    i+=1
n = 5
fact = 1
for i in range(1,n + 1):
    fact = fact * i
print(fact)
a =[]
for i in range(1,11):
    print(i)
    append.a
    print(a)
n = 5
fact = 1
for i in range(1,n+1):
    fact = fact * i
students = {
"student1": {
    "name": "preethi",
    "age" :19,
    "city":"paris"
   
},
"student2" : {
    "name": "kavi",
    "age" :26,
    "city":"US"
      }
}
print(students["course"])

def greet():
    print("hello preethy")
greet()    
 
def greet(a,b):
    print(a+b)
greet(20,89)    

def add(a,b):
    return a * b
print(add(5,4))    
def greet(name,age):
    print("hello",name,age)
greet("preethy",19)   
def greet(country= "india"):
    print("show counrty",country)

greet()
name = "preethy"
age = 18
print(f"my name is {name} and iam {age} years old!")
def add(*args):
    total = 0
    for number in args:
        total +=number
    print(total)
add (10,20,30)        
def student(**kwargs):
    print(kwargs)
student(name= "preethy",age = 19,city = "paris")    
def order_food(*args,**kwargs):
    print("\n Item ordered")
    for item in args:
        print(f"{item}")
    print(f"Delivery detail:sending to {kwargs.get('name')} at {kwargs.get('address')}")        
order_food("pizza","coke",name = "sam",address = "paris")
def count(n):
    if n == 0 :
        return
    print(n)
    count(n-1)
count(5)         

def marksheet(name,html,css,java):
    total = html+ css+ java
    print
def countdown(number):
    if number <= 0:
      print("blast off") 
    else:
     print(number)
     countdown(number-1)
     countdown(10)    
def calculate_total(prices_list):
  total = sum(prices_list)
  print(f"The Total bill is ₹ (total)")
  shoping.cart=[100,200,400]
  calculate_total(shoping.cart)

trainer_name = "kavi"
def print_info():
  topic = "python"
  print (f("trainer_name,topic"))
def print_user_detail(name,city):
  print(f"The Username is {name},They are from {city}")
  print_user_detail("preethy","paris")
def order_food(*args,**kwargs):
    print("\n Item ordered")
    for item in args:
        print(f"{item}")
    print(f"Delivery address:sending to {kwargs.get('name')} at {kwargs.get('address')}")        
order_food("pizza","coke",name = "sam",address = "paris")


    
import turtle

color = ["red","purple",
          "blue","green",
          "orange","yellow"]
cursor = turtle.Turtle()
turtle.bgcolor("black")   

for c in range(360):
      cursor.pencolor(color[c % 6])       
      cursor.width(c/100 + 1)
      cursor.forward(c)
      cursor.left(59)
import turtle
import time

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")

door = turtle.Turtle()
door.shape("square")
door.color("red")
door.shapesize(10, 5)
door.penup()
door.goto(0, 0)


def open_door(x, y):
    door.goto(250, 0)

    earth = turtle.Turtle()
    earth.shape("circle")
    earth.color("blue")
    earth.penup()
    earth.goto(0, 0)

    for size in range(1, 15):
        earth.shapesize(size)
        screen.update()
        time.sleep(0.05)


door.onclick(open_door)

screen.mainloop()
