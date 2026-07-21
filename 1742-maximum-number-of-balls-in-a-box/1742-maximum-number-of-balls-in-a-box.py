class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        #Hint from discusion Tab 
        """
        From the given constraints, we notice that the highest possible ball number is 100.000. That means the ball number 99.999 holds the maximum digit sum of 9∗5=45. That said, instead of using a Mapper object, you can use an array of 46 elements (45−0+1).
        
        """
        def sumofdigits(num) :
            res = 0 
            while num :
                res += num % 10 
                num = num // 10 
            return res
        res = [0] * 46
        for i in range(lowLimit , highLimit + 1) :
            res[sumofdigits(i)] += 1 
        return max(res)
