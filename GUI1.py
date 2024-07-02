import csv
import tkinter as tk
from tkinter import messagebox

def process_transaction():
    PRN = prn_entry.get()
    Merchant = merchant_entry.get()
    Amount = int(amount_entry.get())
    PIN = pin_entry.get()
    flag = 0
    Balance = 0
    
    with open('data2.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if row[1] == PRN:
                flag = 1
                if row[4] == 'Inactive':
                    messagebox.showerror("Error", "User inactive")
                    return
                elif row[4] == 'Active':
                    if(Amount < 0):
                        messagebox.showerror("Error", "Invalid Amount")
                        return
                    if Amount > int(row[2]):
                        messagebox.showerror("Error", "Insufficient balance")
                        return
                    else:
                        if PIN == row[3]:
                            new_balance = int(row[2]) - Amount
                            Balance = new_balance
                            row[2] = str(new_balance)
                            with open('data2.csv', mode='w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(rows)
                            messagebox.showinfo("Success", "New balance: " + str(new_balance))
                        else:
                            messagebox.showerror("Error", "Wrong PIN")
                            return
    if flag == 0:
        messagebox.showerror("Error", "PRN not found")
        return
    new_row = [PRN, Merchant, Amount, Balance]
    with open('transaction.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)
    name = Merchant
    amount = Amount
    if not csv.reader(open('profits.csv', 'r')):
        with open('profits.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Vendor's Name", "Profit"])
    with open('profits.csv', 'r') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            if row[0] == name:
                profit = int(row[1]) + amount
                row[1] = str(profit)
            data.append(row)
    if name not in [row[0] for row in data]:
        data.append([name, str(amount)])
    with open('profits.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Create GUI window
window = tk.Tk()
window.title("Transaction Processing")

# Create GUI elements
prn_label = tk.Label(window, text="PRN:")
prn_entry = tk.Entry(window)
merchant_label = tk.Label(window, text="Merchant Name:")
merchant_entry = tk.Entry(window)
amount_label = tk.Label(window, text="Amount:")
amount_entry = tk.Entry(window)
pin_label = tk.Label(window, text="PIN:")
pin_entry = tk.Entry(window, show="*")
submit_button = tk.Button(window, text="Submit", command=process_transaction)

# Place GUI elements in window
prn_label.grid(row=0, column=0)
prn_entry.grid(row=0, column=1)
merchant_label.grid(row=1, column=0)
merchant_entry.grid(row=1, column=1)
amount_label.grid(row=2, column=0)
amount_entry.grid(row=2, column=1)
pin_label.grid(row=3, column=0)
pin_entry.grid(row=3, column=1)
submit_button.grid(row=4, column=1)

window.mainloop()