import tkinter as tk
from tkinter import messagebox
from database import add_expense, get_expenses, get_total
root = tk.Tk()
root.title("Expance Tracker")

tk.Label(root,text="Title").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root,text="Amount").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root,text="Date").pack()
title_entry = tk.Entry(root)
title_entry.pack()

def save():   
     title = title_entry.get() 
     amount = amount_entry.get()   
     date = date_entry.get()
     if title and Amount and date:
        add_expense(title,float(Amount),date)
        messagebox.showinfo("Succes","Expence Added")
     else:
        messagebox.showerror("Error ","All filed are requried")
tk.Button(root,text="Add Expence",command= save).pack()

result = tk.Listbox(root,width=50)
result.pack

def total():
    t = get_total()
    messagebox.showinfo("Total", f"Total.Expence:₹ {t}")
tk.Button(root,text="Show total",command=total).pack()
root.mainloop()
