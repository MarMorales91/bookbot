def num_of_words(text):
    num_words = len(text.split())
    return num_words

def count_char(texts):
    chars = {}
    for text in texts:
        lower_case = text.lower()
        if lower_case.isalpha() == False:
            continue
        elif lower_case in chars:
            chars[lower_case] += 1
        else:
            chars[lower_case] = 1
    return(chars)

def sort_on(items):
    return items["num"]

def sorted_dic(items):
    sort = []
    for item in items:
        sort.append({"char": item, "num": items[item]})
    sort.sort(reverse=True, key=sort_on)
    return sort
    