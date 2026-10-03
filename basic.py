# name = "preethi"
# age = 19
# subject = "python"
# print(name)
# print(age)
# print(subject)
# name = "preethi"
# age = 19
# college = "P.S.G"
# is_student = True
# print(name)
# print(age)
# print(college)
# print(is_student)
# # print(type(name))
# # print(type(age))
# # print(type(college))
# print(type(is_student))
#  name = input("Enter your name:")
#  print(name)
# age = int(input("Enter your age: "))
# print(type(age))
#  a = 10
#  b = 20
#  print(a + b)
#  print(a - b)
#  print(a * b)
#  print(a / b)
#  print(a % b)
# a = 10
# b = 20
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# name = input("Enter your name:")
# age = input("Enter your age:")
# print(name)
# print(age)
# name = "preethi"
# print(type(name))
# age = 19
# print(type(age))
# age =  int(input("Enter ur age:"))
# print(type(age))
# marks = 70
# if marks>=90:
#     print("Grade-A")
# elif marks>=30:
#         print("Grade-B")
# elif marks>=35:
#      print("Grade-C")


# for i in range(10):
#     print(i)

# i=0
# while i<10:
#     print(i)
#     i+=1
# name = input("Enter your Name:")
# marks = input("Enter your Marks:")
# name = "Preethi"
# tamil = 80
# english = 85
# python = 90

# print("Name:", name)
# print("Tamil:", tamil)
# print("English:", english)
# print("Computer:", computer)
# marks = 100
# if marks>=90:
#      print("Grade-A")
# elif marks>=50:
#       print("Grade-B")
# elif marks>=35:
#      print("Grade-C")
# else:
#      print("Fail")
# mark1 = int(input("Enter Html mark:"))
# mark2 = int(input("Enter Css mark:"))
# mark3 = int(input("Enter Javascript mark:"))
# mark4 = int(input("Enter Java mark:"))
# mark5 = int(input("Enter Python mark:"))
# mark6 = int(input("Enter Bootstracp mark:"))
# total = mark1 + mark2 + mark3 + mark4 + mark5 + mark6
# print("Total=",total)

# for i in range(1,11):
#     print(i)
# for i in range(1,11):
#     if i % 2 ==0:
#      print(i) even num
# for i in range(1,11):
#     if i % 2!= 0:
#      print(i) odd numbers
# for i in range(1,11):
#       if i % 3 == 0:
#        print(i)  
# 
# i = 1
# while i<=5:
#     print(i)
#     i+=1
# i = 0
# while i<=10:
#     print(i)
#     i+=1
# for i in range(1,51):
#     print(i)
# for i in range(15):
#     if i == 5:
#          break
#     print(i)
# for i in range(15):
#      if i == 5:
#            continue
#      print(i)     
# i = ["apple","orange","banana","kiwi"]
# for i in(i):
#       print(i)


# 1-list mutable,ordered,[]
# def marksheet(name, tamil, english, python):
#     total = tamil + english + python
#     average = total / 3

#     print("Name:", name)
#     print("Total:", total)
#     print("Average:", average)

#     if average >= 35:
#         print("Pass")
#     else:
#         print("Fail")


# name = input("Name: ")
# tamil = int(input("Tamil: "))
# english = int(input("English: "))
# python = int(input("Python: "))

# marksheet(name, tamil, english, python)



'''
fruits=['apple','mango','orange']
print(fruits)
fruits.append('kiwi')
print(fruits)
fruits.remove('mango')
print(fruits)

num=[12,45,67,89,34]
print(num)
num.append(34)
print(num)
num.extend([23,46,70,30])
print(num)
num.insert(1,100)
print(num)
num.pop(4)
print(num)
print("max:",max(num))
print("min:",min(num))
print("sum:",sum(num))
num[2]=54
print(num)

for i in friuts:
      print(i)


#tuple immutable 

tup=(12,56,78,90,56)
print(type(tup))
print(tup)


tup_list=list(tup)
print(type(tup_list))

list_tup=tuple(tup_list)

print(len(tup))
print("max:",max(tup))
print("min:",min(tup))
print("sum:",sum(tup))

for i in tup_list:
      print(i)

'''
set {},no duplictes
s1={1,1,2,2,4,5,6,7,8,8}
print(s1)


a={1,2,3,6}
b={6,7,8,9}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

for i in range(4):
      for j in range(3):
            print("*" ,end=" ")
      print()     


      print()      
def calculate_total(price_list):
      total = sum(price_list)
      print(f"The Total Bill is ₹ {total}")
shopping_card = [200,80,600]
calculate_total(shopping_card)      


for i in range(3):
      for j in range(6):
            print("*",end= " ")
      print()
def calculate_total(price):
      total = sum(price)
      print(f"the total bill is ₹ {total}")
amount = [200, 400, 500]
calculate_total(amount)      

def dress_order(*args,**kwargs):
      print("\n dress_order")
      for dress in args:
          print(f"{dress}")
          print(f"delivery detail: sending to {kwargs.get ('name')} at {kwargs.get('address')}")
dress_order("shirt","jeans",name = "preethy",address = "paris") 
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
