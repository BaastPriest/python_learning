# add remove discard pop clear

def unique_characters_1():
    """print number of unique characters of each entered word not case-sensitive"""
    for _ in range(int(input())):
        print(len(set(input().lower())))


def unique_characters_2():
    """displaying the total number of unique characters in all words read, not case-sensitive"""
    characters = set()
    for _ in range(int(input())):
        for c in input().lower():
            characters.add(c)
    print(len(characters))


def sum_of_different_words_in_the_text():
    """find the number of different words in a line of text."""
    # len(set(re.sub(r'[,.?:;!-]', '', input().lower()).split(" ")))
    text = [word.lower().strip('.,;:-?!') for word in input().split()]
    print(len(set(text)))


def has_the_number_been_seen_before():
    """For each number, print the word YES (in a separate line)
    if this number has previously appeared in the sequence or NO if it has not."""
    # numbers = [int(i) for i in input().split()]
    my_set = set()
    for i in input().split():
        if int(i) in my_set:
            print("YES")
        else:
            my_set.add(int(i))
            print("NO")
