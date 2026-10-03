name = input("Enter Student Name: ")

html = int(input("Enter Html Mark: "))
css = int(input("Enter css Mark: "))
java = int(input("Enter Java Mark: "))
bootstracp = int(input("Enter Bootstracp Mark: "))
python = int(input("Enter Python Mark: "))

total = html + css+ java+ bootstracp+ python
ave = total/5

if ave >=50:
    print("Result: PASS")
else:    
    print("Result: FAIL")

print("Student Name:",name)
print("Html:",html)
print("Css:",css)
print("Java:",java)
print("Bootstracp:",bootstracp)
print("Python:",python)

print("Total:",total)
print("Average:",ave)

# if ave >=50:
#     print("Result: PASS")
# else:    
#     print("Result: FAIL")
    

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()
