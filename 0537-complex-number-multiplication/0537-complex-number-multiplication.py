class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        c1 = num1.split("+")
        c2 = num2.split("+") 
        real_part = int(c1[0]) * int(c2[0]) - int(c1[1][:-1]) * int(c2[1][:-1]) 
        complex_part = int(c1[0]) * int(c2[1][:-1]) + int(c2[0]) * int(c1[1][:-1]) 
        return  str(real_part) + "+" + str(complex_part) + "i"