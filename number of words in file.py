def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    file_name = input("Enter the name of the text file: ")
    word_count = count_words(file_name)
    if word_count is not None:
        print(f"Number of words in '{file_name}': {word_count}")

if __name__ == "__main__":
    main()
