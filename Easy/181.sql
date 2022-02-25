-- Employees Earning More Than Their Managers

SELECT a.name as Employee
from Employee as a
join Employee as b
on a.managerId = b.id
        where a.salary > b.salary