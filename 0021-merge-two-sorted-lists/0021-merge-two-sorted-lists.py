# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) 
        res = dummy
        curr1 = list1
        curr2 = list2 
        while curr1 is not None  and curr2 is not  None :
            if curr1.val < curr2.val :
                dummy.next = curr1 
                curr1 = curr1.next 
            else :
                dummy.next = curr2 
                curr2 = curr2.next
            dummy = dummy.next
        while curr1 :
            dummy.next = curr1 
            curr1 = curr1.next  
            dummy = dummy.next
        while curr2 :
            dummy.next = curr2 
            curr2 = curr2.next
            dummy = dummy.next
        return res.next