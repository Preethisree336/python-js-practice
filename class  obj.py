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

class  my_phone:
    def __init__(self,brand,serialno):
        self.brand = brand
        self.__serial__no = serialno

    def get_serialno(self):
        return self.__serial__no  
    
    
p1 = my_phone('vivo','x90123455')
print("secure serialno:",p1.get_serialno())
