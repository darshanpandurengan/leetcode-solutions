# Write your MySQL query statement below
SELECT P.product_name, year, price FROM Sales 
INNER JOIN 
Product P 
ON  P.product_id = Sales.product_id ; 