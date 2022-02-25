# Adding Spaces to a String

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.insert(0, 0)
        words=[s[i:j] for i,j in zip(spaces, spaces[1:]+[None])]
        return " ".join(words)