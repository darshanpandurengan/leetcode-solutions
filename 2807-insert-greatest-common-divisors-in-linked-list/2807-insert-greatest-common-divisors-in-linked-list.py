# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a , b) :
            if b == 0 :
                return a 
            return gcd(b , a % b) 
        res = head
        dummy = res
        curr = head.next 
        while curr is not None :
            a = gcd(res.val , curr.val) 
            res.next = ListNode(a) 
            res = res.next 
            res.next = curr 
            res = res.next 
            curr = curr.next 
        return dummy 