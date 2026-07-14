class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        res = ""
        count  = 0 
        for i in str(num) :
            if i == "6" and count < 1 :
                res += "9"
                count += 1
            else :
                res += i
        return int(res)

        