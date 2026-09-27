class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        if sum(chalk) <= k :
            k = k % sum(chalk) 
        for idx , c in enumerate(chalk) :
            k -= c 
            if k < 0 :
                return idx 