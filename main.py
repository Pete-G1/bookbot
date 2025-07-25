from stats import get_word_count
from stats import get_char_count
from stats import sort_report

def get_book_text(r):
    with open(r) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    test = get_book_text("books/frankenstein.txt")
    characters = get_char_count(test)
    dic = sort_report(characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_word_count(test)
    print("--------- Character Count -------")
    for char in dic:
        item = char["char"]
        if item.isalpha() == True:
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")        
      


main()    


