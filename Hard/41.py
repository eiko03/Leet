# First Missing Positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)

        exist = [False for _ in range(n + 1)]
        print(exists)

        for i in range(1, 2 ** 31):
            if i not in s:
                return i
        return 2 ** 31