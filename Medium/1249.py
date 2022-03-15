# Minimum Remove to Make Valid Parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        paren = ['(',')']
        stack = []
        for idx, char in enumerate(s):
            if char == paren[0]:
                stack.append((char,idx))
            elif char == paren[1]:
                    
                if len(stack)!=0 and stack[-1][0] == paren[0]: 
                    stack.pop()
                    
                else:
                    stack.append((char,idx))
                    
        for i,(char, idx) in enumerate(stack):
            s= s[:idx-i] + s[idx+1-i:]
            
        return s
