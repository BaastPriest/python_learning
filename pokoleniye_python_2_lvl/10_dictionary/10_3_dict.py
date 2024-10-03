def dict_keys_are_num():
    """Write code so that the variable result stores a dictionary in which
    the keys are numbers from 1 to 15 (inclusive) and the values are the squares of the keys."""
    result = {}
    for i in range(1, 16):
        result[i] = i * i
    return result
    # another solution
    # result.setdefault(i, i**2)

def merge_two_dict():
    """Merge the contents of two dictionaries dict1 and dict2:
    if the key is in both dictionaries, add it to the dictionary with a value equal to the sum of the values
    from the first and second dictionaries;
    if the key is in only one of the dictionaries, add it to the dictionary with its current value."""
    dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
    dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
    result = dict2.copy()

    for key1 in dict1:
        if key1 in dict2.keys():
            result[key1] = dict1.get(key1) + dict2.get(key1)
        else:
            result[key1] = dict1.get(key1)
    return result
    # another solution
    #result = dict1.copy()
    #for k, v in dict2.items():
    #    result[k] = result.get(k, 0) + v


def dict_count_char():
    """ so that the result variable stores a dictionary in which the number
    of occurrences of each character in the text string will be counted. """
    text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
    result = {}
    for c in text:
        result[c] = result.get(c, 0) + 1
    return result
    # another solution 1
    # result[c] = result.setdefault(c, 0) + 1
    # another solution 2
    # for k, v in dict1.items():
    #     result[k] = result.get(k, 0) + v
    #
    # for k, v in dict2.items():
    #     result[k] = result.get(k, 0) + v

def dict_mist_frequently_word():
    """output the most frequently occurring word in the string s.
    If there are several such words, the one that is smaller in lexicographic order should be output."""
    s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

    result = {}

    words = s.split(" ")

    for word in words:
        result[word] = result.get(word, 0) + 1

    max_frequency = max(result.values())
    max_words = [word for word, count in result.items() if count == max_frequency]
    min_lex_word = min(max_words)
    return min_lex_word

    # another solution

    #most_common = words_list[0]
    #for word in words_dict.keys():
    #if words_dict[word] > words_dict[most_common]:
    #    most_common = word
    #elif words_dict[word] == words_dict[most_common] and word < most_common:
    #    most_common = word
