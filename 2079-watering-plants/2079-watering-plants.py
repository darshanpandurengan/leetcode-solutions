class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        curr = capacity
        for i in range(len(plants)) :
            steps += 1
            if curr < plants[i] :
                curr = capacity 
                steps += 2 * i 
            curr -= plants[i] 
        return steps 