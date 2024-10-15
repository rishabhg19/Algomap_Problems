# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        first = head
        curr = head
        breakout = False
        while curr:
            currVal = curr.val
            while curr.next and not breakout:
                if currVal == curr.next.val:
                    curr.next = curr.next.next
                else:
                    breakout = True
            curr = curr.next
            breakout = False
        return first
            
        