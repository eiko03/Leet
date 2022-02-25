# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxmap =[0]
        re s =""
        for char in s:
            if char not in res:
                re s+ =char
            else:
                re s =res.split(char, 1)[1 ] +char
            maxmap.append(len(res))
        return max(maxmap)
