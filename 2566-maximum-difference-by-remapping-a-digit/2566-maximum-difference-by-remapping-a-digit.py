class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        min_str = max_str = str(num)
        min_map = None 
        max_map = None 
        for ch in min_str :
            if ch != '0' :
                min_map = ch
                break 
        for ch in max_str :
            if ch != "9" :
                max_map = ch 
                break 
        if max_map is not None :
            maxnum = int(max_str.replace(max_map , "9")) 
        else :
            maxnum = int(max_str)
        if min_map is not None :
            minnum = int(min_str.replace(min_map , "0")) 
        else :
            maxnum = int(min_str)
        return maxnum - minnum