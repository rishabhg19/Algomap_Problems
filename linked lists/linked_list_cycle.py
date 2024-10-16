# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head
        slow = head
        if not fast.next and not slow.next:
            return False
        while fast and slow:
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
            if fast == slow:
                return True
        return False