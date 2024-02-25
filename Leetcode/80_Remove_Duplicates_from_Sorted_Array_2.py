from typing import List


def removeDuplicates(nums: List[int]) -> int:
    count = 0
    num_left = nums[0]
    print(num_left)
    for i in range(len(nums)):
        if count <= 2 and num_left == nums[i]:
            count += 1
            print("count = ", count)
            num_left = nums[i]
        else:
            nums.pop(i)
            print("new nums = ", nums)
            count = 0


removeDuplicates([1, 1, 1, 2, 2, 3])
