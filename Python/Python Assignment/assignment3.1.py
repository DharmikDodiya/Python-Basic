import csv
from tabulate import tabulate

def read_csv_file(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            if not rows:
                print("The CSV file is empty.")
                return

            headers = rows[0]      # First row is the header
            data = rows[1:]        # Remaining rows are data

            print(tabulate(data, headers=headers, tablefmt='grid'))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = input("Enter the path to the CSV file: ")
read_csv_file(file_path)
