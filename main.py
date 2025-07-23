from stats import get_word_count

def get_book_text(r):
    with open(r) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    test = get_book_text("books/frankenstein.txt")
    return test

main()
get_word_count(main())


