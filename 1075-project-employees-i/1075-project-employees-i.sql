# Write your MySQL query statement below
SELECT  p.project_id , AVG(E.experience_years) AS average_years 
FROM Project p INNER JOIN Employee E ON 
p.employee_id = E.employee_id 
GROUP BY p.project_id ; 