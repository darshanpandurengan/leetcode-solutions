class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        for i in range(len(nums)) :
            for j in range(i + 1 , len(nums)) :
                a , b = int(str(nums[i])[0]) , nums[j] % 10 
                while b : 
                    a , b  = b , a % b
                isCoPrime = (a == 1) 
                if isCoPrime :
                    res += 1 
        return res