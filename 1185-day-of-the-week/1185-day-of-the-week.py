class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        """
        Zeller’s Congruence 
        h=(q + ⌊13(m+1)/5​⌋ + K+⌊K/4​⌋ + ⌊J/4​⌋ + 5J ) mod 7
        q = day of the month
        m = month number
        K = last two digits of the year
        J = first two digits of the year 
        h = 0 --> saturday 
        h = 1 --> sunday...
        """
        # January and February are treated as 
        # months 13 and 14 of the previous year
        if month == 1 or month == 2: 
            month += 12 
            year -= 1
        k = int(str(year)[2 : ]) 
        j = int(str(year)[:2])
        h = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7 
        week = ["Saturday" , "Sunday", "Monday", "Tuesday", "Wednesday","Thursday", "Friday" ]
        return week[h]