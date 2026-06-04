import tkinter as tk
from tkinter import ttk
import openpyxl as op
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Simple Purchase Ordering System")
window.configure(bg="lightblue")
window.resizable(False,False)

def works():
    book = op.load_workbook("Alba_Database.xlsx")
    order = book.active

    for row in table.get_children():
        table.delete(row)

    for row in order.iter_rows(min_row=2,values_only=True):
        table.insert("",tk.END,values=row)

def input_validation():
    cname= cname_entry.get()
    prod=product_entry.get()
    qty=int(qty_entry.get())
    price=int(price_entry.get())

    if not cname or not prod or not qty or not price:
        messagebox.showerror("Error","All fields required!")
        return False
    
    return True

def savings():
    if not input_validation():
        return
    
    cname= cname_entry.get()
    prod=product_entry.get()
    qty=int(qty_entry.get())
    price=int(price_entry.get())

    total= qty * price

    workbook = op.load_workbook("Alba_Database.xlsx")
    order=workbook.active

    new_id= order.max_row

    order.append([new_id,cname,prod,qty,price,total])
    workbook.save("Alba_Database.xlsx")

    messagebox.showinfo("Success","Record added successfully!")
    works()

def update():
    select = table.focus()

    if not select:
        messagebox.showerror("Error", "Select a record first")
        return
    
    if not input_validation():
        return
    
    values = table.item(select, "values")
    record_id = int(values[0])

    cname= cname_entry.get()
    prod=product_entry.get()
    qty=int(qty_entry.get())
    price=int(price_entry.get())
    total= qty * price

    workbook = op.load_workbook("Alba_Database.xlsx")
    order = workbook.active

    for row in order.iter_rows(min_row=2):
        if row[0].value == record_id:
            row[1].value = cname
            row[2].value = prod
            row[3].value = qty
            row[4].value = price
            row[5].value = total

    workbook.save("Alba_Database.xlsx")
    messagebox.showinfo("Success","Record updated successfully!")
    works()

def delete():
    selected = table.focus()

    if not selected:
        messagebox.showerror("Error","Select a record first!")

    values = table.item(selected,"values")
    record_id = values[0]

    confirm = messagebox.askyesno("Confirm","Are you sure you want to delete this record?")
    
    if not confirm:
        return

    workbook = op.load_workbook("Alba_Database.xlsx")
    order = workbook.active

    for i,row in enumerate(order.iter_rows(min_row=2),start=2):
        if str(row[0].value) == str(record_id):
            order.delete_rows(i)
            break

    workbook.save("Alba_Database.xlsx")
    messagebox.showinfo("Success","Record deleted successfully")
    works()

def auto_populate(event):
    selected = table.focus()
    values = table.item(selected,"values")

    if values:
        cname_entry.delete(0,tk.END)
        product_entry.delete(0,tk.END)
        qty_entry.delete(0,tk.END)
        price_entry.delete(0,tk.END)

        cname_entry.insert(0,values[1])
        product_entry.insert(0,values[2])
        qty_entry.insert(0,values[3])
        price_entry.insert(0,values[4])

def markets():
    window = tk.Tk()
    window.title("Market Items")
    window.geometry("350x610")
    window.resizable(False,False)

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    table = ttk.Treeview(
        window,
        columns=("Gun Name", "Price ($)"),
        show="headings"
    )

    for headings in ("Gun Name", "Price ($)"):
        table.heading(headings, text=headings)

    guns = [
        ("Glock 19", 550),
        ("Locus", 3900),
        ("Renetti", 500),   
        ("AK47", 700),
        ("DR-H", 4000),
        ("Kilo 141", 4500),
        ("Krig 6", 5000),
        ("QQ9", 3200),
        ("Fennec", 3800),
        ("CBR4", 4200),
        ("DL Q33", 5500),
        ("MAC-10", 1000),
        ("Switchblade X9", 1200),
        ("LAPA", 300),
        ("CX-9", 450),
        ("PP19 Bizon", 2000),
        ("XPR-50", 3005),
        ("Arctic .50", 2500),
        ("M21 EBR", 1500),
        ("NA-45", 7000),
        ("Rytec AMR", 3200),
        ("SVD", 2000),
        ("Koshka", 2000),
        ("LW3-Tundra", 5000),
        ("BY15", 3000),
        ("HS2126", 2300),
        ("Striker", 8900),
        ("KRM-262", 6000),
    ]

    for name, price in guns:
        table.insert("", tk.END, values=(name, price))

    table.grid(row=0, column=0,sticky="nsew", padx=10, pady=10)


# Form Title
title = tk.Label(window, text="Simple Purchase Ordering System", font=("Times New Roman", 14, "bold"), bg="lightblue")
title.grid(row=0, column=0, columnspan=6)

# Frame
genframe = tk.Frame(window, bg="lightblue", bd=2, relief="groove")
genframe.grid(row=1, column=0, columnspan=7, padx=10, pady=10)

# Customer Name Entry
cname_entry = tk.Entry(genframe, font=("Poppins", 12))
cname_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=(10, 0))

cname_label = tk.Label(genframe, text="Customer Name", font=("Poppins", 10, "italic"), bg="lightblue")
cname_label.grid(row=3, column=1, columnspan=2)

# Product Entry
product_entry = tk.Entry(genframe, font=("Poppins", 12))
product_entry.grid(row=2, column=3, columnspan=2, padx=10, pady=(10, 0))

product_label = tk.Label(genframe, text="Product", font=("Poppins", 10, "italic"), bg="lightblue")
product_label.grid(row=3, column=3, columnspan=2)

# Quantity Entry
qty_entry = tk.Entry(genframe, font=("Poppins", 12))
qty_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=(10, 0))

qty_label = tk.Label(genframe, text="Quantity", font=("Poppins", 10, "italic"), bg="lightblue")
qty_label.grid(row=5, column=1, columnspan=2)

# Price Entry
price_entry = tk.Entry(genframe, font=("Poppins", 12))
price_entry.grid(row=4, column=3, columnspan=2, padx=10, pady=(10, 0))

price_label = tk.Label(genframe, text="Price ($)", font=("Poppins", 10, "italic"), bg="lightblue")
price_label.grid(row=5, column=3, columnspan=2)

# Buttons
submit_btn = tk.Button(window, text="Submit", font=("Poppins", 12, "bold"), bg="lightpink", command=savings)
submit_btn.grid(row=6, column=1, pady=(10, 20))

update_btn = tk.Button(window, text="Update",font=("Poppins", 12, "bold"), bg="lightgreen", command=update)
update_btn.grid(row=6, column=2)

delete_btn = tk.Button(window, text="Delete", bg="red", fg="white",font=("Poppins", 12, "bold",),command = delete)
delete_btn.grid(row=6, column=3)

market_btn = tk.Button(window, text="Open Market", bg="yellow", fg="black",font=("Poppins", 12, "bold",),command = markets)
market_btn.grid(row=6, column=4)

# Table
table = ttk.Treeview(
    window,
    columns=("Order ID", "Customer Name", "Product", "Quantity", "Price", "Total"),
    show="headings"
)

for headings in ("Order ID", "Customer Name", "Product", "Quantity", "Price", "Total"):
    table.heading(headings, text=headings)

table.grid(row=7, column=0, columnspan=6, padx=10, pady=10)

table.bind("<<TreeviewSelect>>", auto_populate)
works()

window.mainloop()