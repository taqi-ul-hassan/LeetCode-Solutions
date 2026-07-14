# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        middle_element = count // 2
        
        current = head          # Fix 1: fresh pointer starting from head
        for _ in range(middle_element):   # Fix 2: loop to walk forward, not [] indexing
            current = current.next
        
        return current           # Fix 3: return the node itself