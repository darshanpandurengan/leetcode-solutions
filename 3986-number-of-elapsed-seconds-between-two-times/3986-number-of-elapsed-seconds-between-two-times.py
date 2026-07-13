class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        startHour , startMinute , startSecond = startTime.split(":")
        endtHour , endMinute , endSecond = endTime.split(":")
        totalstarttime = int(startHour) * 3600 + int(startMinute) * 60 + int(startSecond)
        totalendtime = int(endtHour) * 3600 + int(endMinute) * 60 + int(endSecond)
        return totalendtime - totalstarttime
