# Write your MySQL query statement below
SELECT E.name FROM Employee E
INNER JOIN Employee E1 
ON 
E.id = E1.managerId 
GROUP BY  E1.managerId 
HAVING COUNT(*) >= 5 
; 