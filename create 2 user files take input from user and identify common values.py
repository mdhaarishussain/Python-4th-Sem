import csv

def write_to_csv(file_name, data):
    if not data:
        print("No data provided to write into CSV.")
        return

    try:
        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
        print(f"CSV file '{file_name}' created successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

def read_from_csv(file_name):
    data = []
    try:
        with open(file_name, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                data.append(row)
        return data
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def find_common_values(file1_data, file2_data):
    if not file1_data or not file2_data:
        print("No data to compare.")
        return

    common_values = set(map(tuple, file1_data)).intersection(set(map(tuple, file2_data)))
    if common_values:
        print("Common values found:")
        for value in common_values:
            print(list(value))
    else:
        print("No common values found.")

def main():
    file1_name = input("Enter the name of the first CSV file to create (without extension): ") + ".csv"
    file2_name = input("Enter the name of the second CSV file to create (without extension): ") + ".csv"

    file1_data = []
    file2_data = []

    print("Enter data for the first CSV file:")
    while True:
        row = input("Enter comma-separated values for a row (press Enter to stop): ")
        if not row:
            break
        file1_data.append(row.split(','))

    print("Enter data for the second CSV file:")
    while True:
        row = input("Enter comma-separated values for a row (press Enter to stop): ")
        if not row:
            break
        file2_data.append(row.split(','))

    write_to_csv(file1_name, file1_data)
    write_to_csv(file2_name, file2_data)

    file1_data = read_from_csv(file1_name)
    file2_data = read_from_csv(file2_name)

    if file1_data and file2_data:
        find_common_values(file1_data, file2_data)

if __name__ == "__main__":
    main()
