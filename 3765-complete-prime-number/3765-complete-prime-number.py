class Solution(object):
    def isprime(self , num ) :
        if num < 2 :
            return False
        for i in range(2 , int(num**0.5) + 1 ) :
            if num % i == 0:
                return False
        return True 

    def completePrime(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 :
            return False
        temp = str(num) 
        arr = [num % 10] 
        num = num // 10 
        countor = 10 
        while num :
            digit = num % 10 
            arr.append(digit * countor + arr[-1])
            countor *= 10 
            num = num // 10 
        arr.append(temp[0]) 
        for i in range(1 , len(temp)) :
            arr.append(arr[-1] + temp[i])
        for n in arr :
            if not  self.isprime(int(n)) :
                return False
        return True