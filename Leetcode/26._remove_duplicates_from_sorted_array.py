from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i = len(nums)
    nums = set(nums)
    i -= len(nums)
    print(str(i) + ", nums =", list(nums))


removeDuplicates(nums = [1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])