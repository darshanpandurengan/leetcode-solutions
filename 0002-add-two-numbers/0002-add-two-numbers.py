# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) 
        res = dummy
        carry = 0 
        while l1 is not None and l2 is not None :
            total = l1.val + l2.val + carry
            res.next = ListNode(total % 10) 
            res = res.next 
            carry = total // 10 
            l1 = l1.next 
            l2 = l2.next 
        while l1 is not None :
            total = l1.val + carry
            res.next = ListNode(total % 10) 
            res = res.next 
            carry = total // 10 
            l1 = l1.next 
        while l2 is not None :
            total = l2.val + carry
            res.next = ListNode(total % 10) 
            res = res.next 
            carry = total // 10 
            l2 = l2.next
        if carry :
            res.next = ListNode(carry) 
        return dummy.next 