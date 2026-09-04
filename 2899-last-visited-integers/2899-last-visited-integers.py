class Solution(object):
    def lastVisitedIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = []
        ans = [] 
        k = 0 
        for num in nums :
            if num > 0 :
                k = 0
                seen.insert(0 , num)
            else :
                k += 1
                if 0 < k <= len(seen) :
                    ans.append(seen[k - 1])
                elif k > 0 and k > len(seen) :
                    ans.append(-1)
        return ans