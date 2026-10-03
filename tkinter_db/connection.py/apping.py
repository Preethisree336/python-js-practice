import tkinter as tk
from tkinter import messagebox
from database import add_expense,get_expenses,get_total
root = tk.Tk()
root.title("Expance tracker")
root.geometry("400x400")

tk.Label(root,text="Title").pack()

title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root, text="Amount").pack()
amount.entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root,text="Date (DD-MM-YYYY)").pack()
date.entry = tk.Entry(root)
date_entry.pack()


def save():
    title = title_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()
    if title and amount and date:
        add_expense(title)
