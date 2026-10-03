# import threading
# def task1():
#     print("task 1 is completed")
# def task2():
#     print("task 2 is completed")
# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()

# import threading
# def first():
#     for i in range(1,6):
#         print(i)
# def sec():
#     print("python full stack")    
# f1 = threading.Thread(target=first)
# s2 = threading.Thread(target=sec)
# f1.start()
# s2.start()

# import threading
# import time
# def pizza_cook():
#     time.sleep(7)
#     print("Pizza is ready")

# def sauce_cook():
#     time.sleep(3)

#     print("sauce is ready")  
# p1 = threading.Thread(target=pizza_cook)
# s2 = threading.Thread(target=sauce_cook)
# p1.start()
# s2.start() 
# p1.join()
# s2.join()
# print("Dinner is Ready!")


# import threading
# import time
# def coffee():
#     print("coffee is preparing..")
#     time.sleep(0)
#     print("Coffee is Ready☕")
# def Delivery():
#     print("We have taken your order")
#     time.sleep(3)
#     print("Coffee is delivered..📦")
# c1 = threading.Thread(target=coffee)
# d1 = threading.Thread(target=Delivery)
# c1.start()
# d1.start()
# c1.join()
# d1.join ()
# print("Thanks For Your Order!!")    
 
 
import turtle

s = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor('black')
s.pencolor('skyblue')

a = 0
b = 0

s.speed(0)
s.penup()
s.goto(0, 200)
s.pendown()

while True:
    s.forward(a)
    s.right(b)

    a += 3
    b += 1

    if b == 210:
        break

s.hideturtle()
turtle.done()

