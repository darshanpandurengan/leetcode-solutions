class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        res = [] 
        min_abs = float("inf")
        arr.sort() 
        for i in range(len(arr) - 1) :
            if abs(arr[i] - arr[i + 1] ) < min_abs :
                min_abs = abs(arr[i] - arr[i + 1] ) 
                temp = [arr[i] , arr[i + 1] ] 
                res = [] 
                res.append(temp)
            elif abs(arr[i] - arr[i + 1] ) ==  min_abs :
                temp = [arr[i] , arr[i + 1] ] 
                res.append(temp)
        return res