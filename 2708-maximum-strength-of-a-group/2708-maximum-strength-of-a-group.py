class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = [] 
        neg = []
        zero = 0 
        for num in nums :
            if num > 0 :
                pos.append(num)
            elif num < 0 :
                neg.append(num)
            else :
                zero = 1 
        neg.sort() 
        res = 1
        pop = None 
        if pos :
            for num in pos :
                res *= num
        if neg :
            if len(neg) % 2 == 1 :
                pop = neg.pop() 
            for num in neg :
                res *= num 
        if res == 1   :
            if pos :
                return 1
            if neg :
                return 1  
            if zero :
                return 0 
            if len(neg) == 0 and pop is not None :
                return pop
        return res