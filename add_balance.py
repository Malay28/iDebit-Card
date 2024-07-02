import csv

PRN = input("Enter PRN: ")

with open('data2.csv', 'r') as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)
    found = False
    for row in rows:
        if row[1] == PRN:
            found = True
            break
    if found:
        new_amount = input("Enter new amount: ")
        if(new_amount<=0):
            print("Invalid Amount\n")
            exit()
        old_balance = int(row[2])
        new_balance = old_balance + int(new_amount)
        row[2] = str(new_balance)
        with open('data2.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)
    else:
        print("Invalid user")
