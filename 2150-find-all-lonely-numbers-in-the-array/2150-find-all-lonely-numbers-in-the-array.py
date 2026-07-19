class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set(nums)
        d = {}
        res = [] 
        for num in nums :
            if (num - 1) not in seen and (num + 1) not in seen :
                    res.append(num)
            if num not in d :
                d[num] = 1
            else :
                d[num] += 1 
        output = [] 
        for num in res :
            if d[num] == 1 :
                output.append(num)
        return output