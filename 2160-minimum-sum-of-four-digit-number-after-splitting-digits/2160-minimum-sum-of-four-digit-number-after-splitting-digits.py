class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = [] 
        while num :
            arr.append(num % 10)
            num = num // 10
        arr.sort()
        return arr[0] * 10 + arr[2] + arr[1] * 10 + arr[3]