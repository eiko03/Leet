-- Department Top Three Salaries

select Department,Employee,Salary from (
    SELECT d.name as Department,
    e.name as Employee,
    e.salary as Salary,
    dense_rank() Over (
        partition by d.name
        order by salary desc
    ) as sdds
    FROM Department d
    Inner Join Employee e
    On d.id=e.departmentId
) as tbl
where sdds<4