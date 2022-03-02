# Is Subsequent

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
            
        for idx, char in enumerate(s):
            if char in t:
                t = t[t.index(char)+1 : ]
                    
            else: 
                return False;
            
        return True;
