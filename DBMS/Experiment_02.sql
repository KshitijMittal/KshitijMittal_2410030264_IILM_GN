USE company2cse2;

-- Perform Following Query using Employee Table. (Retrieving Data) 
-- 1. List all distinct job in Employee. 
SELECT DISTINCT job FROM employee;

-- 2. List all information about employee in Department Number 30. 
SELECT * FROM employee WHERE deptno = 30;

-- 3. Find all department number with department names greater than 20. 
SELECT * FROM employee WHERE deptno > 20;

-- I don't know where to put.
SELECT deptno, dname FROM department WHERE deptno > 20;

-- 4. Find all information about all the managers as well as the clerks in department 30. 
SELECT * FROM employee WHERE deptno = 30 AND job IN ('MANAGER', 'CLERK');

-- 5. List the Employee name, Employee numbers and department of all clerks. 
SELECT ENAME, EMPNO, DEPTNO FROM employee WHERE job = 'CLERK';

-- 6. Find all managers not in department 30.  
SELECT * FROM employee WHERE job = 'MANAGER' AND deptno <> 30;

-- 7. List information about all Employees in department 10 who are not manager or clerks. 
SELECT * FROM employee WHERE job not in ('MANAGER', 'CLERK') AND deptno = 10;

-- 8. Find Employees and jobs earning between 1200 and 1400. 
SELECT * FROM employee WHERE sal BETWEEN 1200 AND 1400;

-- 9. List Name and Department Number of employee who are clerks, analyst or salesman. 
SELECT ename, deptno FROM employee WHERE job IN ('CLERK', 'SALESMAN', 'ANALYST');

-- 10. List Name and Department Number of employee whose names began with M. 
SELECT ename, deptno FROM employee WHERE ename LIKE 'M%';