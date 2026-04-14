USE company2cse2;

-- 1. Display the list of employees who have joined the company before 30th June 80 or after 31st Dec 81. 
SELECT * FROM employee WHERE hiredate < '1980-06-30' OR hiredate > '1981-12-31';

-- 2. Display the names of employees whose names have second alphabet A in their names. 
SELECT ename FROM employee WHERE ename LIKE '_A%';

-- 3. Display the names of employees whose name is exactly five characters in length.
SELECT ename FROM employee WHERE ename LIKE '_____';
			-- Another way
SELECT ename FROM employee WHERE length(ename) = 5;

-- 4. Display the names of employees whose names have second alphabet A in their names. 
SELECT ename FROM employee WHERE ename LIKE '_A%';

-- 5. Display the names of employees who are not working as salesman or clerk or analyst. 
SELECT ename FROM employee WHERE job NOT IN ('SALESMAN', 'CLERK', 'ANALYST');
			-- Another way
SELECT ename FROM employee WHERE job <> 'SALESMAN' AND job <> 'CLERK' AND job <> 'ANALYST';

-- 6. Display the name of the employee along with their annual salary (sal*12). The name of the employee earning highest salary should appear first. 
SELECT ename, sal*12 AS ANNUAL_SALARY FROM employee order by sal DESC;

-- 7. Display name, sal, hra, pf, da, totalsal for each employee. The output should be in the order of total sal, hra 15% of sal, da 10% of sal, pf 5% of sal. Total salary will be (sal*hra*da)-pf. 
SELECT ename, sal, sal * 0.15 AS hra, sal * 0.10 AS da, sal * 0.05 AS pf,
sal * (sal * 0.15) * (sal * 0.10) - (sal * 0.05) AS total_salary
 FROM employee order by total_salary, hra, da, pf DESC;

-- 8. Update the salary of each employee by 10% increment who are not eligible for commission. 
UPDATE employee SET sal = sal * 1.1 WHERE comm IS NULL OR comm = 0;
SELECT * FROM employee;

-- 9. Display those employees whose salary is more than 3000 after giving 20% increment. 
SELECT * FROM employee WHERE sal * 1.2 > 3000;

-- 10. Display those employees whose salary contains atleast 3 digits. 
SELECT ename, sal FROM employee WHERE sal >= 100;
			-- Another way
SELECT ename, sal FROM employee WHERE length(sal) >= 3;