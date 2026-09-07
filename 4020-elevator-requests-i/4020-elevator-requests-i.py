class Solution(object):
    def elevatorRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        prefix = [0] * len(requests)
        prefix[0] = requests[0]
        for i in range(1 , len(requests)) :
            prefix[i] = abs(requests[i] - requests[i - 1])
        return sum(prefix)