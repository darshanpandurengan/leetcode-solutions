# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        countor = 1 
        oddDummy = ListNode(0) 
        evenDummy = ListNode(0)
        odd = oddDummy
        even = evenDummy 
        curr = head 
        while curr is not None :
            if countor % 2 == 1 :
                odd.next = curr 
                odd = odd.next 
            else :
                even.next = curr 
                even = even.next 
            curr = curr.next 
            countor = 1 - countor 
        even.next = None 
        evenDummy = evenDummy.next 
        odd.next = evenDummy 
        return oddDummy.next