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


def print_student_grades_2():
    """dimensions that occur in no more than two blocks."""
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())
    print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))


def print_student_grades_3():
    """grades of the third student that are not found in either the first or the second student."""
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())
    print(*sorted(set3 - (set1 | set2), reverse=True))


def print_student_grades_4():
    """grades not found in any of the three students."""
    all_grades_set = {int(i) for i in range(11)}
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())
    print(*sorted(all_grades_set - (set1 | set2 | set3)))
