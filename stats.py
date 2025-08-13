def words_counter(text):
    return len(text.split())

def char_counter(text):
    chars_dict = {}
    text = text.lower()

    for char in text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    return chars_dict

def sort_on(dict):
    return dict['num']

def sort_dict(dict):
    pair_dict = []
    for el in dict:
        pair_dict.append({
            'char': el,
            'num': dict[el]
        })
    pair_dict.sort(reverse=True,key=sort_on)
    return pair_dict
