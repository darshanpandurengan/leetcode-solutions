class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        prev = timeSeries[0] 
        res = duration
        for i in range(1 , len(timeSeries)) :
            if prev + duration >= timeSeries[i] :
                res += timeSeries[i] - prev 
            else :
                res += duration 
            prev = timeSeries[i] 
        return res