# Reverse Linked List

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nextHead = head.next
            head.next = prev
            prev = head
            head = nextHead
        return prev