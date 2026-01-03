import sys

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents
    
from stats import get_book_words, get_book_characters, sort_numbers

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_book_words(text)
    num_characters = get_book_characters(text)
    num_sorted = sort_numbers(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")      
    for item in num_sorted:
        letter = item["char"]
        count = item["num"]
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============== END ==============")
    

main()

