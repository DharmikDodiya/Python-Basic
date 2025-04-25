import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            # Read and print the header
            headers = next(csv_reader)
            print(f"Headers: {headers}")
            
            # Read and print the rows
            print("\nRows:")
            for row in csv_reader:
                print(row)
                
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
if __name__ == "__main__":
    file_path = input("Enter the CSV file path: ")
    read_csv(file_path)
