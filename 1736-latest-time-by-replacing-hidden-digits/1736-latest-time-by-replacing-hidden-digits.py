class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        res = [] 
        for i in time :
            if i != ":" :
                res.append(i)
        time = res
        if time[0] == "?" :
            if time[1] == "?" :
                time[0] = "2"
                time[1] = "3"
            elif int(time[1]) > 3 :
                time[0] = "1"
            else :
                time[0] = "2"
        if time[1] == "?" :
            if time[0] == "2" :
                time[1] = "3"
            else :
                time[1] = "9"
        if time[2] == "?" :
            time[2] = "5"
        if time[3] == "?" :
            time[3] = "9"
        return "".join(time[:2]) + ":" + "".join(time[2:])