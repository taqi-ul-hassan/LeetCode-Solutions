# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp is not None:
            temp = temp.next
            count +=1
        middle = count//2
        # suppose middle = 3
        temp = head
        for i in range(middle):
            temp = temp.next
        return temp

        