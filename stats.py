

def get_word_count(test):
    count = test.split()
    word_count = len(count)
    print(f"Found {word_count} total words")
#counts total words in book. 

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
#returns a dictionary of characters and how often they appear.
def sort_on(items):
    return items["num"]  
 #helper function for sort_report 

def sort_report(report_data):
    report_list = []
    for char, num in report_data.items():
        temp = {"char":char, "num": num}
        report_list.append(temp)
    report_list.sort(reverse=True, key=sort_on)
    return report_list
 #turns dictionary of characters and their counts into a list of dictionaries of characters and their counts.    
        
    




    






