class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd , even = [] , [] 
        countor = 0 
        for i in range(len(nums)) :
            if countor == 0 :
                even.append(nums[i])
            else :
                odd.append(nums[i])
            countor = 1 - countor 
        odd.sort(reverse = True)
        even.sort()
        res = [] 
        for i in range(max(len(odd) , len(even))) :
            if i < len(even) :
                res.append(even[i])
            if i < len(odd) :
                res.append(odd[i])
        return res