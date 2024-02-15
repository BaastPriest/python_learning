def unique_values_numbers():
    items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
    my_set = set()
    for c in items:
        my_set.add(int(c))

    print(*sorted(my_set))


def first_letter_of_each_word_lowercase():
    words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes',
             'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
    my_set = set()
    for w in words:
        my_set.add(w[0].lower())

    print(*sorted(my_set))


sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, 
    save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory,
     over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: 
     surely, you all know those redolent remnants of day suspended, with the midges, 
     about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, 
     in the summer dusk; a furry warmth, golden midges.'''


def unique_words_lowercase(sentence):
    """Print the result on one line in alphabetical order, separating elements with one space character"""
    words_set = set(word.lower().strip("(),:;.") for word in sentence.split(" "))
    print(*sorted(words_set))


def unique_words_lowercase_len_less_4_symbols(sentence):
    words_set = set(word.lower().strip("(),:;.") for word in sentence.split(" "))
    words_set = set(word for word in words_set if len(word) < 4)
    print(*sorted(words_set))
    """ words = {
    word.strip('.,:():;!?').lower()
    for word in sentence.split()
    if len(word.strip('.,:():;!?')) < 4 }"""


def unique_file_names_with_png_extensions():
    files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG', 'solution.Py', 'stepik.org',
             'kotlin.ko', 'github.git', 'ZeBrA.PnG']
    my_file_set = set(file_name.lower() for file_name in files if file_name[-4:].lower() == ".png")
    print(*sorted(my_file_set))
    """png_files = {file.lower() for file in files if file.lower().endswith('.png')}"""
