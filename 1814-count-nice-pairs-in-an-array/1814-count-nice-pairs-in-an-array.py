class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reverse(num) :
            return int(str(num)[::-1])
        d = {}
        for num in nums :
            temp = num - reverse(num)
            if temp not in d :
                d[temp] = 1
            else :
                d[temp] += 1 
        ans = 0 
        for v in d.values() :
            ans += v * (v - 1) // 2 #nc2 
        return ans % (10**9 + 7)