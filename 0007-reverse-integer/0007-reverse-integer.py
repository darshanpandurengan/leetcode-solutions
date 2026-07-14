class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_number = 0 
        sign = 1 
        if x < 0 :
            sign = -1
        absolute_number = abs(x)
        while absolute_number :
            digit = absolute_number % 10 
            reverse_number = reverse_number * 10 + digit
            absolute_number = absolute_number // 10 
        reverse_number *= sign 
        print(reverse_number )
        if  -2**31 <= reverse_number <= 2**31 - 1 :
            return reverse_number 
        return 0