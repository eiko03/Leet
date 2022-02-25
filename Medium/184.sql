-- Department Highest Salary

WITH highestSalByDept AS (

    SELECT
        departmentId,
        MAX(salary) AS mxS
    FROM
        employee
    GROUP BY
        departmentId

)

SELECT
    t3.name AS "Department",
    t1.name AS "Employee",
    t1.salary AS "Salary"
FROM
    employee t1
INNER JOIN
    highestSalByDept t2
ON
    t1.departmentId = t2.departmentId AND t1.salary = t2.mxS
INNER JOIN
    department t3
ON
    t1.departmentId = t3.id;
