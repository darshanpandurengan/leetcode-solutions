# Write your MySQL query statement below
SELECT C.name as Customers from Customers C where C.id NOT IN ( 
    select customerId 
    FROM Orders 
) ; 