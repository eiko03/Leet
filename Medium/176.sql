-- Second Highest Salary

SELECT IFNULL(
    (
        SELECT DISTINCT salary FROM Employee
        order by  salary desc
        limit 1,1
    ), NULL )
AS SecondHighestSalary ;