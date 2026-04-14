USE company2cse2;

-- 1. Display the total number of employee working in the company. 
SELECT count(*) AS total_employee FROM employee;

-- 2. Display the total salary being paid to all employees. 
SELECT sum(sal) AS total_salary FROM employee;

-- 3. Display the maximum salary from employee table. 
SELECT max(sal) AS maximum_salary FROM employee;

-- 4. Display the minimum salary from employee table. 
SELECT min(sal) AS minimum_salary FROM employee;

-- 5. Display the average salary from employee table.
SELECT avg(sal) AS average_salary FROM employee;

-- 6. Display the maximum salary being paid to clerk. 
SELECT max(sal) AS clerk_max_salary FROM employee WHERE job = 'CLERK';

-- 7. Display the maximum salary being paid in dept no 20. 
SELECT max(sal) AS deptno_20_max_salary FROM employee WHERE deptno = 20;

-- 8. Display the minimum salary paid to any salesman. 
SELECT min(sal) AS minimum_sal_to_salesman FROM employee WHERE job = 'SALEMAN';

-- 9. Display the average salary drawn by managers. 
SELECT avg(sal) AS manager_average_salary FROM employee WHERE job = 'MANAGER';

-- 10. Display the total salary drawn by analyst working in dept no 40. 
SELECT sum(sal) AS analyst_total_salary FROM employee WHERE job = 'ANALYST' AND deptno = 40;

-- 11. Display the names of the employee in Uppercase. 
SELECT upper(ename) AS uppercase FROM employee;

-- 12. Display the names of the employee in Lowercase. 
SELECT lower(ename) AS lowercase FROM employee;

-- 13. Display the names of the employee in Proper case. 
SELECT initcap;

-- 14. Display the length of Your name using appropriate function.
SELECT length('Kshitij') AS kshitij_length;
 
-- 15. Display the length of all the employee names. 
SELECT ename, length(ename) AS length_of_employee_names FROM employee;