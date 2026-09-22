class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def GCD(a , b) :
            while b :
                a , b  = b , a % b
            return a 
        res = [] 
        for i in range(1 , n) :
            for j in range(2 , n + 1) :
                if GCD(i , j) == 1 and i < j  :
                    res.append(str(i) + "/" + str(j)) 
        return res 