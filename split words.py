def split_words(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                print("Words in the line:")
                for word in words:
                    print(word)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    file_name = input("Enter the name of the text file: ")
    split_words(file_name)

if __name__ == "__main__":
    main()
