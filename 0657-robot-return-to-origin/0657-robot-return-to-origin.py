class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u = d = l = r = 0 
        for ch in moves :
            if ch == "U" :
                u += 1 
            elif ch == "D" :
                d += 1 
            elif ch == "L" :
                l += 1 
            else :
                r += 1 
        return l == r and u == d 