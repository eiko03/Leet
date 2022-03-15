#  Maximum Number of Coins You Can Get

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum([ x for i,x in enumerate(sorted(piles,reverse=True)[:(len(piles)//3)*2]) if(i!=0 and i%2 != 0) ]) 
