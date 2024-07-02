import csv
import os
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
def update_balance():
    PRN = prn_entry.get()
    new_amount = amount_entry.get()
    if not PRN:
        messagebox.showerror("Error", "Please enter PRN")
        return
    if not new_amount:
        messagebox.showerror("Error", "Please enter new amount")
        return
    try:
        new_amount = int(new_amount)
        if new_amount <= 0:
            messagebox.showerror("Error", "Invalid amount")
            return
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    with open('data2.csv', 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        found = False
        for row in rows:
            if row[1] == PRN:
                found = True
                old_balance = int(row[2])
                new_balance = old_balance + new_amount
                row[2] = str(new_balance)
                with open('data2.csv', 'w', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
                messagebox.showinfo("Success", f"Balance updated for PRN {PRN}. New balance is {new_balance}")
                break
        if not found:
            messagebox.showerror("Error", "User not found")
def append_data():
    # Get user input values
    prn = prn_entry.get()
    balance = balance_entry.get()
    pin = pin_entry.get()
    status = status_entry.get()

    # Validate input values
    if not prn:
        messagebox.showerror("Error", "Please enter PRN")
        return
    try:
        balance = int(balance)
        if balance < 0:
            messagebox.showerror("Error", "Invalid balance amount")
            return
    except ValueError:
        messagebox.showerror("Error", "Balance must be a number")
        return
    if not pin:
        messagebox.showerror("Error", "Please enter PIN")
        return
    if not status:
        messagebox.showerror("Error", "Please enter status")
        return

    # Get the new serial number
    with open('data2.csv', 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        last_row = rows[-1]
        last_serial_number = int(last_row[0])
        new_serial_number = last_serial_number + 1

    # Append the new row to the CSV file
    with open('data2.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_serial_number, prn, balance, pin, status])
    messagebox.showinfo("Success", "Values have been appended to the CSV file.")

while True:
    print("What would you like to do?")
    print("1. Scan Bar Code")
    print("2. Add Balance to your Wallet")
    print("3. Add a new user")
    print("4. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
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
    elif choice == '2':
        root = tk.Tk()
        root.title("Balance Updater")

        # Create input fields and labels
        prn_label = tk.Label(root, text="PRN:")
        prn_entry = tk.Entry(root)
        amount_label = tk.Label(root, text="New Amount:")
        amount_entry = tk.Entry(root)

        # Create update button
        update_button = tk.Button(root, text="Update Balance", command=update_balance)

        # Layout GUI
        prn_label.grid(row=0, column=0, padx=5, pady=5)
        prn_entry.grid(row=0, column=1, padx=5, pady=5)
        amount_label.grid(row=1, column=0, padx=5, pady=5)
        amount_entry.grid(row=1, column=1, padx=5, pady=5)
        update_button.grid(row=2, column=1, padx=5, pady=5)

        root.mainloop()

    elif choice == '3':
        # Create GUI
        root = tk.Tk()
        root.title("CSV Appender")

        # Create input fields and labels
        prn_label = tk.Label(root, text="PRN:")
        prn_entry = tk.Entry(root)
        balance_label = tk.Label(root, text="Balance:")
        balance_entry = tk.Entry(root)
        pin_label = tk.Label(root, text="PIN:")
        pin_entry = tk.Entry(root)
        status_label = tk.Label(root, text="Status:")
        status_entry = tk.Entry(root)

        # Create append button
        append_button = tk.Button(root, text="Append to CSV", command=append_data)

        # Layout GUI
        prn_label.grid(row=0, column=0, padx=5, pady=5)
        prn_entry.grid(row=0, column=1, padx=5, pady=5)
        balance_label.grid(row=1, column=0, padx=5, pady=5)
        balance_entry.grid(row=1, column=1, padx=5, pady=5)
        pin_label.grid(row=2, column=0, padx=5, pady=5)
        pin_entry.grid(row=2, column=1, padx=5, pady=5)
        status_label.grid(row=3, column=0, padx=5, pady=5)
        status_entry.grid(row=3, column=1, padx=5, pady=5)
        append_button.grid(row=4, column=1, padx=5, pady=5)

        root.mainloop()

    elif choice == '4':
        exit()
    else:
        print("Invalid choice, please try again.")
