# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head,head
        prev = None

        if not head or not head.next:
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None #break 

        l1 = head
        l2 = second
        a = None
        while l2:
            tmp = l2.next
            l2.next = a
            a = l2
            l2 = tmp 
        l2 = a

        while l2:
            tmp1,tmp2 = l1.next,l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2




