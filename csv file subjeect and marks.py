import csv
def read_csv_file(filename):
    subjects = []
    marks = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists
        for row in reader:
            subjects.append(row[0])
            marks.append(int(row[1]))

    return subjects, marks
def create_dictionary(subjects, marks):
    data_dict = {}
    for i in range(len(subjects)):
        data_dict[subjects[i]] = marks[i]
    return data_dict

def main():
    filename = 'Book1.csv'
    subjects, marks = read_csv_file(filename)
    data_dict = create_dictionary(subjects, marks)

    print("Dictionary created:")
    print(data_dict)

if __name__ == "__main__":
    main()
