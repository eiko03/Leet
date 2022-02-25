# Add Two Numbers

class Solution:


    def lin(self ,res=1 ,l1 ,l2):
        if l1 != None and l2 != None:
            # print(res.val)
            res =ListNode(l1.val+ l2.val)
            self.lin(res.next ,l1.next, l2.next)
        return res


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.lin(l1 ,l2)
