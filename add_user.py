import csv

with open('data2.csv', 'r') as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)
    last_row = rows[-1]
    last_serial_number = int(last_row[0])
    new_serial_number = last_serial_number + 1
    #print(new_serial_number)

# Ask the user for input values
serial_no = new_serial_number
prn = input("Enter PRN: ")
balance = int(input("Enter Balance: "))
if(balance<0):
    print("Invalid Balance Amount")
    exit()
four_digit_num = input("Enter 4-digit PIN number: ")
status = input("Enter Status: ")


# Define the file path and open the CSV file for appending
file_path = 'path/to/your/csv/file.csv'
with open('data2.csv', 'a', newline='') as csvfile:
    # Create a CSV writer object and write the user input values as a new row
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([serial_no, prn, balance, four_digit_num, status])

#print("Values have been appended to the CSV file.")
