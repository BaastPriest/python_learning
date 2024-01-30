"""
set1 <= set2
set1.issubset(set2)    True or False

set1 >= set2
set1.issuperset(set2)  True or False

set1 < set2   set1 <= set2 and set1 != set2

set1 > set2     set1 >= set2 and set1 != set2

set1.issuperset(list1) BUT print(set1 >= list1) will be error
"""

def is_any_identical_digits_in_two_numbers():
    """YES if the data record contains identical digits and NO if not."""
    set1, set2 = set(input()), set(input())
    if set1.isdisjoint(set2):
        print("NO")
    else:
        print("YES")
    # print('NO' if set(input()).isdisjoint(set(input())) else 'YES')

def is_set1_is_superset_for_set2():
    set1, set2 = set(input()), set(input())
    if set1.issuperset(set2):
        print("YES")
    else:
        print("NO")
    # print(['NO', 'YES'][set(input()) >= set(input())])


def print_student_grades_1():
    """print the grades that both the first and second students have, but which the third student does not."""
    student_1, student_2, student_3 = set(input().split()), set(input().split()), set(input().split())
    print(*sorted(student_1 & student_2 - student_3, reverse=True, key=int))

