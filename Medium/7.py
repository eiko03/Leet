# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        pos =1
        if x < 0:
            x=str(abs(x))[0:]
            pos= -1
        else:
            x=str(x)
        v=0
        for i in range(1,len(x)+1):
            v+=int(int(x[len(x)-i])* (10**(len(x)-i)))
        if v < 2 ** 31:
            return int(v)*pos
        else:
            return 0