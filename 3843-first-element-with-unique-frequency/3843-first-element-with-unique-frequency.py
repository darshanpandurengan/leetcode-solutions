class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums :
            if num not in freq :
                freq[num] = 1 
            else :
                freq[num] += 1 
        freq_freq = {}
        for num in freq.values() :
            if num not in freq_freq :
                freq_freq[num] = 1
            else :
                freq_freq[num] += 1 
        for key in nums :
            if freq_freq[freq[key]] == 1 :
                return key
        return -1