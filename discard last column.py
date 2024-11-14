def read_excel_file(file_name):
    data = []
    with open('Table.csv', 'r') as file:
        for line in file:
            row = line.strip().split(',')
            data.append(row[:-1])  # Discard the last column
    return data

def write_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        for row in data:
            csv_row = ','.join(row) + '\n'
            file.write(csv_row)

def main():
    excel_file = "data.csv"  # Change this to the path of your Excel file
    csv_file = "output.csv"  # Change this to the desired name of your CSV file

    # Read data from Excel file
    data = read_excel_file(excel_file)

    # Write data to CSV file
    write_to_csv(data, csv_file)

    print(f"Data has been successfully written to '{csv_file}' file after discarding the last column.")

if __name__ == "__main__":
    main()
