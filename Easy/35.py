# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums = list(filter((target).__ge__, nums))
        res = None
        if target not in nums:
            return len(nums)

        else:
            for idx, val in enumerate(nums):
                if val == target:
                    res = idx
            return res
