# Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        
        prev=intervals[0]
        
        for list in intervals[1:]:
            if list[0]<=prev[1]:
                prev=[prev[0],max(prev[1],list[1])]
                
            else:
                res.append(prev)
                prev=list
        
        res.append(prev)
        return res
