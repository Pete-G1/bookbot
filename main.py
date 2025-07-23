def get_book_text(r):
    with open(r) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    test = get_book_text("books/frankenstein.txt")
    return test

main()

def get_word_count(test):
    count = test.split()
    word_count = len(count)
    print(f"{word_count} words found in the document")

get_word_count(main())