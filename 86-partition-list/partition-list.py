# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dumy1 = ListNode(0)
        dumy2 = ListNode(0)
        prev1 = dumy1
        prev2 = dumy2
        temp = head  
        temp2 = dumy2
        while temp is not None:
            if temp.val < x:
                prev1.next = temp
                prev1 = prev1.next
            elif temp.val >= x:
                prev2.next = temp
                prev2 = prev2.next
            temp = temp.next
        prev1.next = temp2.next
        prev2.next = None
        return dumy1.next
        

    
