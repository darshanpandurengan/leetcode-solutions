class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res = [first]
        for num in encoded :
            res.append(num ^ res[-1])
        return res