# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) 
        curr = head
        res = dummy 
        count = 0
        temp_sum = 0
        while curr is not None :
            if curr.val == 0 :
                if count % 2 == 1 :
                    dummy.next = ListNode(temp_sum) 
                    dummy = dummy.next
                    temp_sum = 0 
                else :
                    count += 1  
            else :
                if count > -1 :
                    temp_sum += curr.val 
            curr = curr.next 
        return res.next 