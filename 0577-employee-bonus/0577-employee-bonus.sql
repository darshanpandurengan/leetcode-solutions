# Write your MySQL query statement below
SELECT E.NAME , B.Bonus FROM Employee E 
LEFT JOIN  Bonus B 
ON B.empId = E.empId 
WHERE B.bonus is NULL 
OR 
B.bonus < 1000; 