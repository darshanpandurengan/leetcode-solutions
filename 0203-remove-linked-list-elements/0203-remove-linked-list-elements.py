# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1) 
        res = dummy 
        curr = head 
        while curr is not None :
            if curr.val != val :
                res.next = curr 
                res = res.next 
            curr = curr.next 
        res.next = None 
        return dummy.next