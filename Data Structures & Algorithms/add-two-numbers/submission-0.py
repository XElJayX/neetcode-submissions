# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, second =l1,l2
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            print("1")
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1+v2 + carry
            carry = 0
            if sum>=10:
                carry = 1
                sum = sum%10
            
            if l1:
                l1 = l1.next
            if l2:
                l2= l2.next
            val = ListNode(sum%10)
            dummy.next = val
            dummy = dummy.next
        return curr.next