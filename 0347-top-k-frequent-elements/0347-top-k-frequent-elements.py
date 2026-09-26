class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums :
            if num not in freq :
                freq[num] = 1 
            else :
                freq[num] += 1 
        heap = [] 
        for key , value in freq.items() :
            heap.append([value , key]) 
        heap.sort(reverse = True) 
        return [row[1] for row in heap[ : k]]