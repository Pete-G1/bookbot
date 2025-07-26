from stats import get_word_count
from stats import get_char_count
from stats import sort_report
import sys

def get_book_text(r):
    with open(r) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    try:
        test = get_book_text(sys.argv[1])
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    characters = get_char_count(test)
    dic = sort_report(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_word_count(test)
    print("--------- Character Count -------")
    for char in dic:
        item = char["char"]
        if item.isalpha() == True:
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")        
      


main()    


