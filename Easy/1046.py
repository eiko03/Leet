# Last Stone Weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            differ = stones[-1] - stones[-2]
            stones = stones[:len(stones)-2] 
            if differ != 0:
                stones.append(differ)
                stones.sort()
        if len(stones) == 1: return stones[0]
        return 0
