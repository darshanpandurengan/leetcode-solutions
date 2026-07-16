class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a , b) :
            if b == 0 :
                return a
            return gcd(b , a % b )
        prefixGcd = [] 
        mx = 0 
        for num in nums :
            mx = max(mx , num)
            prefixGcd.append(gcd(mx , num))
        res = 0 
        prefixGcd.sort()
        left , right = 0 , len(prefixGcd) - 1
        while left < right :
            res += gcd(prefixGcd[right] ,prefixGcd[left])
            left += 1 
            right -= 1 
        return res