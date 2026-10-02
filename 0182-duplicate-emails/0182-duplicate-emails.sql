# Write your MySQL query statement below
SELECT email AS Email from Person group by email having count(*) > 1 ; 