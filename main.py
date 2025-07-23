from stats import get_word_count, get_char_count, sort_dict

def get_book_text(f): 
    file_contents = f.read()
    return file_contents

def main():
    path_to_book = "books/frankenstein.txt"
    with open(path_to_book) as f:
        words = get_book_text(f)
    num_words = get_word_count(words)
    char_count_dict = get_char_count(words)  # rtn's a dict of {'char' : int}
    sorted_list = sort_dict(char_count_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")


    print("----------- Word Count ----------")
    print(f"Found {num_words} total words ")
    #print(get_char_count(words))
    print("--------- Character Count -------")
    for k, v in sorted_list:
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")


main()