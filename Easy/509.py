# Fibonacchi series

class Solution:
    def execute(self,n,adj_dict):
        if n == 0:
            return 0
        elif n <=2:
            return 1
        elif adj_dict.get(n,False):
            return adj_dict[n]
        else:
            adj_dict[n]= self.execute(n-1,adj_dict)+self.execute(n-2,adj_dict)
            return adj_dict[n]
        
    def fib(self, n: int) -> int:
        adj_dict = {}
        return self.execute(n,adj_dict)
