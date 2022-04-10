# Baseball Game

class Solution:

    def calPoints(self, ops: List[str]) -> int:
        sumary = []
        for op in ops:
            if op == "+":
                sumary.append(int(sumary [-1])+ int(sumary[-2]))
                
            elif op == "C":
                sumary = sumary [:len(sumary)-1]
                
            elif op == "D":
                sumary.append(2 * sumary[-1]) 
                
            else:
                sumary.append(int(op))
                
        return sum(sumary)
