# # mark1 = int(input("Enter Html mark:"))
# # mark2 = int(input("Enter Css mark:"))
# # mark3 = int(input("Enter Javascript mark:"))
# # mark4 = int(input("Enter Java mark:"))
# # mark5 = int(input("Enter Python mark:"))
# # mark6 = int(input("Enter Bootstracp mark:"))
# # total = mark1 + mark2 + mark3 + mark4 + mark5 + mark6
# # print("Total=",total)
# fruits = ["apple","banana","mango"]
# for fruit in fruits:
#      print(fruit)
# numbers = [10,15,20,25,30,45,90,80]
# total = 0
# for  number in numbers:
#     if number % 2 != 0:
#        total = total + number
# print(total)
# tup = (90,0,56,67,98,90)
# tup_list = list(tup)
# print(tup_list)
# numbers = {10,20,30,40}
# numbers.discard(50)
# print(numbers)
# a = {10,20,30}
# b = {10,20,30,40,50}
# print(a.union(b))
# tup = (12,34,45,67,77)
# tup_list = list (tup)
# print (type(tup_list))
# a = 0
# b = 1
# n = 5
# for n in range(1,n+1):  
#  a=b
#  b=c
#  print(n)



# result = []
# for i in range(1,11):
#     result.append(i)
# print("result =",result)    
# def calculate_total(food_price):
#     total = sum(food_price)
#     print(f"The Food Price is ₹ {total}")
# price = [200,80] 
# calculate_total(price)   

# def count_down(n):
#     if n<=0:
#       print("blast off")
#     else:
#         print(n)
#         count_down(n-1)    
# count_down(5)   
# def order_food(*args,**kwargs):
#     print("\n Item ordered")
#     for item in args:
#        print(f"{item}")
#        print(f"Delivery detail:sending to {kwargs.get('name')} at {kwargs.get('address')}")        
# order_food("pizza","coke",name = "sam",address = "paris")
def order_dress(*args,**kwargs):
  print("\n dress_order")
  for dress in args:
     print(f"{dress}")
  print(f"delivery detail: send to {kwargs.get('name')} at {kwargs.get ('address')} at {kwargs.get('phone_num')}")  
order_dress("kurti","croptops","shirt","jeans",name = "preethy",address = "paris",phone_num = 8056680990)