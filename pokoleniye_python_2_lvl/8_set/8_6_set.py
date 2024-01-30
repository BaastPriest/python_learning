# &, |, -, ^
# return new set:
# A.union(B)         A | B
# A.intersection(B)  A & B
# A.difference(B)    A - B
# A.symmetric_difference(B)  A ^ B

# return same set
# A.update(B)               A |= B
# A.intersection_update(B)  A &= B
# A.difference_update(B)   A -= B
# A.symmetric_difference_update(B) A ^= B

def count_of_matching_numbers():
    """find the count of numbers that are in both the first line and the second."""
    # print(len(set(input().split()) & set(input().split())))
    text_1 = set(int(i) for i in input().split())
    text_2 = set(int(i) for i in input().split())
    print(len(text_1.intersection(text_2)))


def print_all_common_numbers_in_ascending_order():
    """all common numbers in ascending order"""
    numbers_1 = set(int(i) for i in input().split())
    numbers_2 = set(int(i) for i in input().split())
    print(*sorted(numbers_1 & numbers_2))


def print_first_line_numbers():
    """all numbers in ascending order that are in the first line but not in the second."""
    line_1 = set(int(i) for i in input().split())
    line_2 = set(int(i) for i in input().split())
    print(*sorted(line_1 - line_2))


def all_common_digits():
    """all common digits in ascending order for all entered numbers."""
    for i in range(int(input())):
        if i == 0:
            my_set = set(input())
        else:
            new_set = set(input())
            my_set.intersection_update(new_set)
            new_set.clear()
    print(*sorted(my_set))
    # n = int(input())
    # numbers = [input() for _ in range(n)]
    # num_set = set(numbers[0]).intersection(*numbers)
    # print(*sorted(num_set))
