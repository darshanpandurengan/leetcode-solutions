class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = [True] * len(candies) 
        mx = max(candies) 
        for idx , candie in enumerate(candies) :
            if candie + extraCandies < mx :
                res[idx] = False
        return res