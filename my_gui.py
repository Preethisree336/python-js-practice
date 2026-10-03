import tkinter as tk
window = tk.Tk()

window.title("my first app")
window.geometry("300x200")

label = tk.Label(window,text= "hloo preethy")
label.pack()

button = tk.Button(window,text= "click me")
button.pack()
window.mainloop()

                        #  ------------ checkbox---------------
import tkinter as tk

root = tk.Tk()

root.title("checkbox examplee")
root.geometry("300x200")

agree = tk.BooleanVar()
check = tk.Checkbutton(root,text= "I agree",variable=agree)
check.pack()
root.mainloop()
print(agree.get())

import tkinter as tk
root = tk.Tk()
root.title("checkbox")
agree = tk.BooleanVar()
check = tk.Checkbutton(root,text="rember me",variable=agree)
check.pack()
root.mainloop()
print(agree.get())

                    # ------------Radiobutton-----------
import tkinter as tk
root = tk.Tk()

root.title("radio button")

chioce = tk.StringVar()

r1 = tk.Radiobutton(root,text="pizza",variable=chioce,value="pizza")
r1.pack()

r2 = tk.Radiobutton(root,text="Burger",variable=chioce,value="Burger")
r2.pack()

root.mainloop()
print(chioce.get())


                           # ------------- list_box--------------------
import tkinter as tk
root = tk.Tk()

listbox = tk.Listbox(root)
listbox.insert(1,"python")
listbox.insert(2,"javascript")
listbox.insert(3,"css")
listbox.insert(4,"tkinter")

listbox.pack()
root.mainloop()

                   #       ----------- scrollbar---------------
import tkinter as tk

root = tk.Tk()

listbox = tk.Listbox(root, height=5)
listbox.pack(side="left")

scroll = tk.Scrollbar(root)
scroll.pack(side="right", fill="y")

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

for i in range(1, 21):
    listbox.insert(tk.END, "Item " + str(i))

root.mainloop()

                           # -------------Menu--------------
import tkinter as tk
root = tk.Tk()
menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)

menu.add_cascade(label= "File",menu=filemenu)

filemenu.add_command(label="New")
filemenu.add_command(label= "Open..")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)

root.mainloop()

import tkinter as tk
root = tk.Tk()

menu = tk.Menu(root)

menu.add_command(label="New")
menu.add_command(label="Open")
menu.add_command(label="Exit",command=root.quit)
root.config(menu=menu)
root.mainloop()

                      # -------Message box--------

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
def show_msg():
    messagebox.showinfo("Message","Hii Preethi!!!")
button= tk.Button(root,text="Click Me..",command=show_msg) 
button.pack()
root.mainloop()   
                    # --------Entry--------------

import tkinter as tk
root = tk.Tk()
 
entry = tk.Entry(root)
entry.pack()
def show_msg():
    user_input = entry.get()
    print(user_input)
button = tk.Button(root,text="submit",command=show_msg)
button.pack()
root.mainloop()     


            #  --------combobox--------------
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
combo = ttk.Combobox(root,values=["Python","Java Script","Css"])
combo.pack()
root.mainloop()

        #    ----------- Scale------------
import tkinter as tk
root = tk.Tk()
scale = tk.Scale(root, from_=0,to=100) 
scale.pack()
root.mainloop() 

import tkinter as tk
root = tk.Tk()
scale = tk.Scale(root,from_=0,to=100,orient=tk.VERTICAL)
scale.pack()
root.mainloop()

              # ----------Top level-----------

from tkinter import *
root = Tk()
root.title('tkinter')
top = Toplevel()
top.title('Python')
top.mainloop()
 
              