# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

    # Advance fast pointer so there is a gap of n between fast and slow
        for _ in range(n + 1):
            fast = fast.next

    # Move both until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

    # slow.next is the node to be removed
        slow.next = slow.next.next

        return dummy.next