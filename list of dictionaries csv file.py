import csv

def write_dicts_to_csv(data):
    if not data:
        print("No data provided to write into CSV.")
        return

    # Get the field names from the first dictionary
    field_names = list(data[0].keys())

    # Get the file name from the user
    file_name = input("Enter the name of the CSV file to save (without extension): ") + ".csv"

    try:
        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)
        print(f"CSV file '{file_name}' created successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    data = []
    while True:
        record = {}
        print("Enter record details (press Enter to stop):")
        for field_name in input("Enter field names separated by comma: ").split(','):
            record[field_name.strip()] = input(f"Enter value for '{field_name.strip()}': ")
        data.append(record)
        if input("Do you want to add another record? (yes/no): ").lower() != 'yes':
            break

    write_dicts_to_csv(data)

if __name__ == "__main__":
    main()
