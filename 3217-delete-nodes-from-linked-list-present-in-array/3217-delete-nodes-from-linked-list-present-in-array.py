# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        dummy = ListNode(0)
        res = dummy
        curr = head 
        while curr is not None :
            if curr.val not in nums :
                dummy.next = curr 
                dummy = dummy.next
            curr = curr.next
        dummy.next = None 
        return res.next