class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        preference = skill[0] + skill[-1] # Setting inital value for comparision
        chemistry  = skill[0] * skill[-1] # Setting initial chemistry 
        left , right = 1 , len(skill) - 2 
        while left < right : 
            if skill[left] + skill[right] != preference :
                return -1
            else :
                chemistry  += skill[left] * skill[right]
            left += 1 
            right -= 1 
        return chemistry 