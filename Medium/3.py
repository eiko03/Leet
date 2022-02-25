# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxmap =[0]
        res =""
        for char in s:
            if char not in res:
                res += char
            else:
                res =res.split(char, 1)[1 ] +char
            maxmap.append(len(res))
        return max(maxmap)
