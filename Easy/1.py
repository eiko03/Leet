# Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = [(num, index)  for index, num in enumerate(nums) if num<=target]
        num_to_index.sort()

        left, right = 0, len(num_to_index) - 1
        while left < right:
            if num_to_index[left][0] + num_to_index[right][0] == target:
                return [num_to_index[left][1], num_to_index[right][1]]
            elif num_to_index[left][0] + num_to_index[right][0] < target:
                left += 1
            else:
                right -= 1