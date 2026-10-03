# name = input("Enter Student Name: ")

# html = int(input("Enter Html Mark: "))
# css = int(input("Enter css Mark: "))
# java = int(input("Enter Java Mark: "))
# bootstracp = int(input("Enter Bootstracp Mark: "))
# python = int(input("Enter Python Mark: "))

# total = html + css+ java+ bootstracp+ python
# ave = total/5

# print("\n------STUDENT MARKSHEET------")

# print("Student Name:",name)
# print("Html:",html)
# print("Css:",css)
# print("Java:",java)
# print("Bootstracp:",bootstracp)
# print("Python:",python)

# print("Total:",total)
# print("Average:",ave)

# if ave >=50:
#     print("Result: PASS")
# else:    
#     print("Result: FAIL")
    

import tkinter as tk

window = tk.Tk()
window.title("Student Worksheet")
window.geometry("400x500")

tk.Label(window, text="Student Worksheet").pack()

tk.Label(window, text="Student Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Tamil").pack()
tamil_entry = tk.Entry(window)
tamil_entry.pack()

tk.Label(window, text="English").pack()
english_entry = tk.Entry(window)
english_entry.pack()

tk.Label(window, text="Maths").pack()
maths_entry = tk.Entry(window)
maths_entry.pack()

tk.Label(window, text="Science").pack()
science_entry = tk.Entry(window)
science_entry.pack()

tk.Label(window, text="Computer").pack()
computer_entry = tk.Entry(window)
computer_entry.pack()

def calculate():
    tamil = int(tamil_entry.get())
    english = int(english_entry.get())
    maths = int(maths_entry.get())
    science = int(science_entry.get())
    computer = int(computer_entry.get())

    total = tamil + english + maths + science + computer
    average = total / 5

    result_label.config(
        text=f"Total: {total}\nAverage: {average}"
    )

tk.Button(window, text="Calculate", command=calculate).pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()