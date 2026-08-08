# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dumy1 = ListNode(0)
        dumy2 = ListNode(0)
        less1 = dumy1
        great2 = dumy2
        temp = head
        while temp is not None:
            if temp.val < x:
                less1.next = temp
                less1 = less1.next
            elif temp.val >= x:
                great2.next = temp
                great2 = great2.next
            temp = temp.next
        less1.next = dumy2.next
        great2.next = None
        return dumy1.next
