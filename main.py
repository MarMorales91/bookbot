import sys
from stats import num_of_words
from stats import count_char
from stats import sorted_dic

def get_books_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

    


def main():
    file = ""
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file = sys.argv[1]
    file_content = get_books_text(file)
    num_words = num_of_words(file_content)
    num_char = count_char(file_content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars = sorted_dic(num_char)
    for char in chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END =============")


main() 