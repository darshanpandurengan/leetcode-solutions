class Solution(object):
    def nearestDrone(self, drones, target):
        """
        :type drones: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        def ManhattanDistance(x1 , y1 , tx1 , ty1) :
            return abs(x1 - tx1) + abs(y1 - ty1) 
        res = float("inf") 
        index = -1
        tx1 = target[0]
        ty1 = target[1]
        countor = 0
        for x1 , y1 , range in drones :
            temp =  ManhattanDistance(x1 , y1 , tx1 , ty1)
            if temp <= range and temp < res :
                index = countor 
                res = ManhattanDistance(x1 , y1 , tx1 , ty1)
            countor += 1 
        return index