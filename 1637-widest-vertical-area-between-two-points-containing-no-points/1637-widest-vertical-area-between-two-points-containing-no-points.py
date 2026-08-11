class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        max_width = 0
        prev_abscissa = points[0][0] 
        for abscissa , ordinate in points[1 : ] :
            if prev_abscissa != abscissa :
                if (abscissa - prev_abscissa  > max_width) :
                    max_width = abscissa - prev_abscissa
                prev_abscissa = abscissa 
        return max_width