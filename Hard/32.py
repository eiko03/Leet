# Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = [[None,0]]
        ans = 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append([c,0])
            else:
                if stack and stack[-1][0]=='(':
                    stack[-2][1]+=2+stack[-1][1]
                    ans=max(ans,stack[-2][1])
                    stack.pop()
                else:
                    stack.append([None,0])
        return ans