class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum_of_digits = 0 
        temp = x 
        while temp :
            sum_of_digits += temp % 10 
            temp = temp // 10 
        if x % sum_of_digits == 0  :
            return sum_of_digits 
        return -1 