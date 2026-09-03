class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        seenA = set()
        seenB = set() 
        res = [] 
        for num1 , num2 in zip(A , B) :
            seenA.add(num1)
            seenB.add(num2)
            res.append(len(seenA.intersection(seenB))) 
        return res