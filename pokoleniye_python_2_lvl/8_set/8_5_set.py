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
