def get_book_words(book):
    num_words = book.split()
    return len(num_words)

def get_book_characters(text):
    characters = {}
    for c in text:
        c = c.lower()
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters
    
def sort_numbers(characters):
    numbers_list = []
    for key, value in characters.items():
        new_dict = {"char": key, "num": value}
        numbers_list.append(new_dict)
    numbers_list.sort(reverse=True, key=sort_on)   
    return numbers_list

def sort_on(numbers_list):
    return numbers_list["num"]

