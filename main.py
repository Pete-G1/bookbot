from stats import get_word_count
from stats import get_char_count

def get_book_text(r):
    with open(r) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    test = get_book_text("books/frankenstein.txt")
    get_word_count(test)
    characters = get_char_count(test)
    print(characters)
    return test

main()    


