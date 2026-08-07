# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        res = dummy
        c = 0
        v1 = 0
        v2 = 0
        while l1 or l2 or c:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            t = v1 + v2 + c
            c = t // 10
            s = t % 10
            dummy.next = ListNode(s)
            dummy = dummy.next
        return res.next


        