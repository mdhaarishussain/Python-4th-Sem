def copy_file_with_uppercase(input_file, output_file):
    try:
        with open(input_file, 'r') as input_f:
            with open(output_file, 'w') as output_f:
                for line in input_f:
                    output_f.write(line.upper())
        print(f"Content copied from '{input_file}' to '{output_file}' with lowercase converted to uppercase.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    input_file = input("Enter the name of the input text file: ")
    output_file = input("Enter the name of the output text file: ")
    copy_file_with_uppercase(input_file, output_file)

if __name__ == "__main__":
    main()
