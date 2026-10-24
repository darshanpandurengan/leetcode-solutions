# Write your MySQL query statement below
SELECT B.book_id  , B.title , B.author , B.genre , B.publication_year ,
B.total_copies AS current_borrowers  
FROM library_books B INNER JOIN borrowing_records R 
ON B.book_id = R.book_id 
WHERE R.return_date IS NULL 
GROUP BY B.book_id 
HAVING COUNT(*) = B.total_copies 
ORDER BY B.total_copies DESC , B.title ; 