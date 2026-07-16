class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        def countOcuurence(num , digit) :
            if num == 0 and digit == 0 :
                return 1
            count = 0 
            while num :
                temp = num % 10 
                if temp == digit :
                    count += 1 
                num = num // 10 
            return count 
        res = 0 
        for num in nums :
            res += countOcuurence(num , digit) 
        return res