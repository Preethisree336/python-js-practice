file =open("student.txt","r")
for a in file:
    print(a.strip())

file.close()

with open("student.txt","w") as a:
    a.write("hloo")

with open("student.txt","r") as file:
    for my in file:
        print(my.strip())
    # file.write("\n Iam learning python full stack")
with open("marks.txt","w") as f1:
    f1.write("85\n")

    f1.write("90\n")
    f1.write("75")
with open("marks.txt","r") as myfile:
    for files in myfile:
        print(files.strip())