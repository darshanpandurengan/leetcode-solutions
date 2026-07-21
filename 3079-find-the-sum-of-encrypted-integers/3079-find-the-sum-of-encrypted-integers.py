class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def encrypt(num) :
            max_digit = 0 
            digits = 0 
            while num :
                max_digit = max(max_digit , num % 10)
                digits = digits * 10 + 1  
                num = num // 10
            return max_digit * digits 
        res = 0 
        for num in nums :
            res += encrypt(num)
        return res