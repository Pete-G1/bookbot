

def get_word_count(test):
    count = test.split()
    word_count = len(count)
    print(f"{word_count} words found in the document")

def get_char_count(test):
    char_count = {
    }
    first_count = test.lower()

    for letter in first_count:
        if letter in char_count:
            char_count[letter] = char_count[letter]+1
        else:
            char_count[letter] = 1

    return char_count

  





