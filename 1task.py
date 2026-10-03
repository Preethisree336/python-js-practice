class Student:
    def __init__(self,name,age,mark):
        self.name = name
        self.age = age
        self.__mark = mark
    def get_mark(self):
        return self.__mark
    def set_mark(self,new_mark):
        self.__mark = new_mark
s1=Student("preethi",19,80)
print(s1.name)
print(s1.age)
print(s1.get_mark())  
s1.set_mark(90)
print(s1.get_mark())  

class CollegeStudent(Student):
    def __init__(self,name,age,mark,course):
        self.name = name
        self.age = age
        self.mark = mark
        self.course = course
c1=CollegeStudent("Preethy",19,90,"Python FullStack Developer")
print(c1.name)
print(c1.age)
print(c1.mark)
print(c1.course)



