class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_output = []

        for j in range(len(nums)):
            for i in range(j, len(nums)):
                if i != j:
                    if nums[j] + nums[i] == target:
                        my_output.append(j)
                        my_output.append(i)
                        break
        return my_output