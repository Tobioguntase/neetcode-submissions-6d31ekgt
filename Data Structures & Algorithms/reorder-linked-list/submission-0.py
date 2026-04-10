# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        s = f = head 

        while f and f.next:
            s = s.next
            f = f.next.next

        prev = None
        curr = s.next
        s.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first = head
        sec = prev
        while sec:
            temp1 = first.next
            temp2 = sec.next
            first.next = sec
            sec.next = temp1
            first = temp1
            sec = temp2
        