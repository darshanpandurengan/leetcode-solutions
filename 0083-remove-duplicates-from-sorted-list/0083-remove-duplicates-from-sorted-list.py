# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-101)
        res = dummy 
        curr = head
        while curr is not None :
            if curr.val != res.val :
                res.next = curr 
                res = res.next
            curr = curr.next
        res.next = None 
        return dummy.next