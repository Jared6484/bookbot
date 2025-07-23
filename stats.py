def get_word_count(f):
    word_list = f.split()
    word_count = len(word_list)
    return word_count

def get_char_count(f):
    book_lowered = f.lower()
    counts ={}
    for char in book_lowered:
        if char in counts:
            counts[char] +=1
        else:
            counts[char] = 1
    return counts

def sort_dict(counts_dict):
    sorted_list = sorted(counts_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_list
