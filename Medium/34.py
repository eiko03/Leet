# Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1 ,-1]
        keys=[k for k,v in enumerate(nums) if v == target]
        return [min(keys), max(keys)]