# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr is not None:
            curr = curr.next
            count+=1
        curr = head
        middle_value = count//2
        for i in range(middle_value):
            curr = curr.next
        return curr

        