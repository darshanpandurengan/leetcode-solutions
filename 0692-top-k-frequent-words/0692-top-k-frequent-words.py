class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = {}
        for word in words :
            if word not in freq :
                freq[word] = 1 
            else :
                freq[word] += 1 
        heap = [] 
        for key , value in freq.items() :
            heap.append([value , key]) 
        heap.sort(key=lambda x: (-x[0], x[1])) 
        return [row[1] for row in heap[:k]]