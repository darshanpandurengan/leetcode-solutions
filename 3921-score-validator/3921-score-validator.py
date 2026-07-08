class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """
        score , counter  = 0 , 0 
        for event in events :
            if event.isdigit() :
                score += int(event)
            elif event == "W" :
                counter += 1
                if counter == 10 :
                    return [score , counter]
            else :
                score += 1 
        return [score , counter]