# Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_ans=[]
        ans=[]
        for s in strs:
            sortedstr="". join(sorted(s))
            if sortedstr not in sorted_ans:
                sorted_ans.append(sortedstr)
                ans.append([s])
            else:
                idx=sorted_ans.index(sortedstr)
                ans[idx].append(s)
        return ans