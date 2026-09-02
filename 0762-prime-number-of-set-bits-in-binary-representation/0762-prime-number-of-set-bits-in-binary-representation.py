class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def isprime(binary) :
            num = binary.count("1")
            prime_set = { 2 , 3, 
                        5 , 7 , 11 ,
                        13 , 17 , 19
            }
            return num in prime_set
        res = 0 
        for j in range(left , right + 1) :
            if isprime(bin(j)[2 : ]) :
                res += 1 
        return res