import random
import csv

data = []

# Generate 200 rows of data
for i in range(1, 999):
    # Generate data for each column
    row = [
        i,  # Serial number
        f"PES2202100{i:03d}",  # Data in format PES2202100501 TO PES2202100700
        random.randint(100, 500),  # Random values between 100 to 500
        random.randint(1000, 9999),  # Random 4-digit number values
        random.choice(["Active", "Inactive"])  # Randomly select "Active" or "Inactive"
    ]
    data.append(row)

# Save data as CSV file
with open("data2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Serial Number", "Data", "Random Value", "4-Digit Number", "Status"])
    writer.writerows(data)
