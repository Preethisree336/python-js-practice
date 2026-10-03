Even or Odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


 number is Positive, Negative, or Zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

Largest of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is largest")
else:
    print(b, "is largest")

    largest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a, "is largest")
elif b > a and b > c:
    print(b, "is largest")
else:
    print(c, "is largest")


total and average of 5 subject marks.

tamil = int(input("Enter Tamil mark: "))
english = int(input("Enter English mark: "))
maths = int(input("Enter Maths mark: "))
science = int(input("Enter Science mark: "))
computer = int(input("Enter Computer mark: "))

total = tamil + english + maths + science + computer
average = total / 5

print("Total:", total)
print("Average:", average)

Factorial Program

num = int(input("Enter a number: "))
fact = 1
for i in range(1,num +1):
    fact = fact * i


print("Factorial:", fact)

num = 5
fact = 1

for i in range(1, 6):
    fact = fact * i

print("Factorial:", fact)


Fibonacci Series Program

n = int(input("Enter number : "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = units * 2
else:
    bill = units * 3

print("Electricity Bill:", bill)


sum of number

numbers = [10, 20, 30, 40, 50]
total = 0
for i in numbers:
    total = total + i

print("Sum:", total)