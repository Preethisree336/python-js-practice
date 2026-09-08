a = 10
fact = 1
for i in range(1, a + 1):
    fact = fact * i
print(fact)

# Factorial using while loop

n = 5
fact = 1

while n > 0:
    fact = fact * n
    n = n - 1
print("While =", fact)