USE company2cse2;

-- 1. Display empno, ename, deptno from employee table. Instead of display department numbers display the related department name (Use decode function).
SELECT empno, ename, case deptno 
WHEN 10 THEN 'RESEARCH' 
WHEN 20 THEN 'ACCOUNTING'
WHEN 30 THEN 'SALES'
WHEN 40 THEN 'OPERATIONS'
ELSE 'UNKNOWN'
END AS dname FROM employee;

-- 2. Display your age in days.
SELECT datediff(curdate(), '2007-03-30') AS Age_in_days;
			-- OR
SELECT datediff(now(), '2007-03-30') AS Age_in_days;

-- 3. Display your age in months.
SELECT timestampdiff(month, '2007-03-30', curdate()) AS Age_in_months;

-- 4. Display the current date as 15th August Friday Nineteen Ninety-Seven.
-- 5. Display the following output for each row from employee table.
-- 6. Scott has joined the company on Wednesday 13th August Nineteen Ninety.
-- 7. Find the date for nearest Saturday after current date.
SELECT date_add(curdate(), INTERVAL 7 - dayofweek(curdate()) + 
(CASE WHEN dayofweek(curdate()) = 7 THEN 7 else 0 END) DAY)
AS Next_Saturday; 

-- 8. Display current time.
SELECT curtime() AS Current_time_;

-- 9. Display the date three months Before the current date.
SELECT date_add(curdate(), INTERVAL -3 MONTH) AS Past_date;
				-- OR
SELECT date_sub(curdate(), INTERVAL 3 MONTH) AS Past_date;

-- 10. Display those employees who joined in the company in the month of Dec.
SELECT * FROM employee WHERE month(hiredate) = 12;
				-- OR
SELECT * FROM employee WHERE monthname(hiredate) = 'DECEMBER';
				-- OR
SELECT * FROM employee WHERE date_format(hiredate, '%M') = 'DECEMBER';
				-- OR
SELECT * FROM employee WHERE date_format(hiredate, '%m') = 12;

-- 11. Display those employees whose first 2 characters from hire date -last 2 characters of salary.
-- 12. Display those employees whose 10% of salary is equal to the year of joining.
SELECT * FROM employee WHERE(sal * 0.10) = year(hiredate);
				-- OR
SELECT * FROM employee WHERE date_format(hiredate, '%Y') = 0.1 * sal;
				-- OR
SELECT * FROM employee WHERE date_format(hiredate, '%y') = 0.1 * sal;
				-- OR
SELECT * FROM employee WHERE year(hiredate) = 0.1 * sal;

-- 13. Display those employees who joined the company before 15 of the months.
SELECT * FROM employee WHERE day(hiredate) < 15; 
				-- OR
SELECT * FROM employee WHERE date_format(hiredate, '%d') < 15;

-- 14. Display those employees who has joined before 15th of the month.
SELECT * FROM employee WHERE day(hiredate) < 15; 
				-- OR
SELECT * FROM employee WHERE date_format(hiredate, '%d') < 15;

-- 15. Display those employees whose joining DATE is available in deptno.
SELECT * FROM employee WHERE day(hiredate) IN (10,20,30,40); 