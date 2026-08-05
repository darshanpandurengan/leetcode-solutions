class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        temp = list(score)
        temp.sort(reverse = True)
        d = {num : idx for idx , num in enumerate(temp) } 
        res = [] 
        for num in score :
            if d[num] == 0 :
                res.append("Gold Medal")
            elif d[num] == 1 :
                res.append("Silver Medal")
            elif d[num] == 2 :
                res.append("Bronze Medal")
            else :
                res.append(str(d[num] + 1 ))
        return res