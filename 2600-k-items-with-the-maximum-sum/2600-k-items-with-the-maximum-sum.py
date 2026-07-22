class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        if k <= numOnes + numZeros :
            return min(k , numOnes)
        return numOnes - (k - numOnes - numZeros)