# DataBase Management System (DBMS)

<div style="border: 2px solid black; padding: 10px; margin: 10px 0;">
<table border="1" cellspacing="0" cellpadding="4" style="border-collapse: collapse; width: 100%; font-size: 12px;">
<thead>
<tr>
<th style="width: 50px;">S.No.</th>
<th>Programs</th>
<th style="width: 70px; white-space: nowrap;">CO No.</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top" align="center">1</td>
<td valign="top">
Table as per given constraints.<br><br>
<strong>Table : EMPLOYEE</strong>
<table border="1" cellspacing="0" cellpadding="5" width="100%">
<tr>
<th>Column Name</th><th>Data Type</th><th>Size</th><th>Attributes</th>
</tr>
<tr><td>EMPNO</td><td>Number</td><td>4</td><td>Primary Key</td></tr>
<tr><td>ENAME</td><td>Varchar2</td><td>20</td><td>Not Null</td></tr>
<tr><td>JOB</td><td>Varchar2</td><td>20</td><td></td></tr>
<tr><td>MGR</td><td>Number</td><td>4</td><td></td></tr>
<tr><td>HIREDATE</td><td>Date</td><td></td><td></td></tr>
<tr><td>SAL</td><td>Number</td><td>10</td><td></td></tr>
<tr><td>COMM</td><td>Number</td><td>7</td><td></td></tr>
<tr><td>DEPTNO</td><td>Number</td><td>2</td><td>Foreign Key</td></tr>
</table>
<br>
<strong>Table : DEPARTMENT</strong>
<table border="1" cellspacing="0" cellpadding="5" width="100%">
<tr>
<th>Column Name</th><th>Data Type</th><th>Size</th><th>Attributes</th>
</tr>
<tr><td>Deptno</td><td>Number</td><td>2</td><td>Primary Key</td></tr>
<tr><td>Dname</td><td>Varchar2</td><td>15</td><td>Not Null</td></tr>
</table>
<br>
<strong>Values in the table.</strong><br>
<strong>EMPLOYEE</strong>
<table border="1" cellspacing="0" cellpadding="5" width="100%">
<tr>
<th>EMPNO</th><th>ENAME</th><th>JOB</th><th>MGR</th><th>HIREDATE</th><th>SAL</th><th>COMM</th><th>DEPTNO</th>
</tr>
<tr><td>7369</td><td>SMITH</td><td>CLERK</td><td>7902</td><td>17-Dec-80</td><td>800</td><td></td><td>20</td></tr>
<tr><td>7499</td><td>ALLEN</td><td>SALESMAN</td><td>7698</td><td>20-Feb-81</td><td>1600</td><td>300</td><td>30</td></tr>
<tr><td>7521</td><td>WARD</td><td>SALESMAN</td><td>7698</td><td>22-Feb-81</td><td>1250</td><td>300</td><td>30</td></tr>
<tr><td>7566</td><td>JONES</td><td>MANAGER</td><td>7839</td><td>02-Apr-81</td><td>2975</td><td></td><td>20</td></tr>
<tr><td>7654</td><td>MARTIN</td><td>SALESMAN</td><td>7698</td><td>28-Sep-81</td><td>1250</td><td>1400</td><td>30</td></tr>
<tr><td>7698</td><td>BLAKE</td><td>MANAGER</td><td>7839</td><td>01-May-81</td><td>2850</td><td></td><td>30</td></tr>
<tr><td>7782</td><td>CLARK</td><td>MANAGER</td><td>7839</td><td>09-Jun-81</td><td>2450</td><td></td><td>20</td></tr>
<tr><td>7788</td><td>SCOTT</td><td>ANALYST</td><td>7566</td><td>09-Dec-82</td><td>3000</td><td></td><td>40</td></tr>
<tr><td>7839</td><td>KING</td><td>PRESIDENT</td><td></td><td>17-Nov-81</td><td>5000</td><td></td><td>20</td></tr>
<tr><td>7844</td><td>TURNER</td><td>SALESMAN</td><td>7698</td><td>08-Sep-81</td><td>1500</td><td>0</td><td>30</td></tr>
<tr><td>7876</td><td>ADAMS</td><td>CLERK</td><td>7788</td><td>12-Jan-83</td><td>1100</td><td></td><td>20</td></tr>
<tr><td>7900</td><td>JAMES</td><td>CLERK</td><td>7698</td><td>03-Dec-81</td><td>950</td><td></td><td>30</td></tr>
<tr><td>7902</td><td>FORD</td><td>ANALYST</td><td>7566</td><td>03-Dec-81</td><td>3000</td><td></td><td>20</td></tr>
<tr><td>7934</td><td>MILLER</td><td>CLERK</td><td>7782</td><td>23-Jan-82</td><td>1300</td><td></td><td>10</td></tr>
</table>
<br>
<strong>DEPARTMENT</strong>
<table border="1" cellspacing="0" cellpadding="5" width="100%">
<tr><th>DEPTNO</th><th>DNAME</th></tr>
<tr><td>10</td><td>RESEARCH</td></tr>
<tr><td>20</td><td>ACCOUNTING</td></tr>
<tr><td>30</td><td>SALES</td></tr>
<tr><td>40</td><td>OPERATIONS</td></tr>
</table>
<br>
<strong>Perform following Query</strong><br>
1. Create Employee_master table with data using Employee table.<br>
2. Delete all record into Employee_master whose DeptNo is 10.<br>
3. Update 10% in his salary of DEPTNO 20 into Employee_Master.<br>
4. Alter SAL with size 10,2 in Employee_Master.<br>
5. Drop Employee_master Table.<br>
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">2</td>
<td valign="top">
<strong>Perform Following Query using Employee Table. (Retrieving Data)</strong><br>
1. List all distinct job in Employee.<br>
2. List all information about employee in Department Number 30.<br>
3. Find all department number with department names greater than 20.<br>
4. Find all information about all the managers as well as the clerks in department 30.<br>
5. List the Employee name, Employee numbers and department of all clerks.<br>
6. Find all managers not in department 30.<br>
7. List information about all Employees in department 10 who are not manager or clerks.<br>
8. Find Employees and jobs earning between 1200 and 1400.<br>
9. List Name and Department Number of employee who are clerks, analyst or salesman.<br>
10. List Name and Department Number of employee whose names began with M.
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">3</td>
<td valign="top">
1. List all employees and jobs in Department 30 in descending order by salary.<br>
2. List job and Department Number of employees whose name are five letters long begin with “A” and end with “N”.<br>
3. Display the name of employees whose name start with alphabet S.<br>
4. Display the names of employees whose name ends with alphabet S.<br>
5. Display the names of employees working in department number 10 or 20 or 40 or employees working as clerks, salesman or analyst.<br>
6. Display employee number and names for employees who earn commission.<br>
7. Display employee number and total salary for each employee.<br>
8. Display employee number and annual salary for each employee.<br>
9. Display the names of all employees working as clerks and drawing a salary more than 3,000.<br>
10. Display the names of employees who are working as clerk, salesman or analyst and drawing a salary more than 3,000.
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">4</td>
<td valign="top">
1. Display the list of employees who have joined the company before 30th June 80 or after 31st Dec 81.<br>
2. Display the names of employees whose names have second alphabet A in their names.<br>
3. Display the names of employees whose name is exactly five characters in length.<br>
4. Display the names of employees whose names have second alphabet A in their names.<br>
5. Display the names of employees who are not working as salesman or clerk or analyst.<br>
6. Display the name of the employee along with their annual salary (sal*12). The name of the employee earning highest salary should appear first.<br>
7. Display name, sal, hra, pf, da, totalsal for each employee. The output should be in the order of total sal, hra 15% of sal, da 10% of sal, pf 5% of sal. Total salary will be (sal*hra*da)-pf.<br>
8. Update the salary of each employee by 10% increment who are not eligible for commission.<br>
9. Display those employees whose salary is more than 3000 after giving 20% increment.<br>
10. Display those employees whose salary contains atleast 3 digits.
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">5</td>
<td valign="top">
1. Display the total number of employee working in the company.<br>
2. Display the total salary being paid to all employees.<br>
3. Display the maximum salary from employee table.<br>
4. Display the minimum salary from employee table.<br>
5. Display the average salary from employee table.<br>
6. Display the maximum salary being paid to clerk.<br>
7. Display the maximum salary being paid in dept no 20.<br>
8. Display the minimum salary paid to any salesman.<br>
9. Display the average salary drawn by managers.<br>
10. Display the total salary drawn by analyst working in dept no 40.<br>
11. Display the names of the employee in Uppercase.<br>
12. Display the names of the employee in Lowercase.<br>
13. Display the names of the employee in Proper case.<br>
14. Display the length of Your name using appropriate function.<br>
15. Display the length of all the employee names.
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">6</td>
<td valign="top">
1. Display empno, ename, deptno from employee table. Instead of display department numbers display the related department name (Use decode function).<br>
2. Display your age in days.<br>
3. Display your age in months.<br>
4. Display the current date as 15th August Friday Nineteen Ninety-Seven.<br>
5. Display the following output for each row from employee table.<br>
6. Scott has joined the company on Wednesday 13th August Nineteen Ninety.<br>
7. Find the date for nearest Saturday after current date.<br>
8. Display current time.<br>
9. Display the date three months Before the current date.<br>
10. Display those employees who joined in the company in the month of Dec.<br>
11. Display those employees whose first 2 characters from hire date -last 2 characters of salary.<br>
12. Display those employees whose 10% of salary is equal to the year of joining.<br>
13. Display those employees who joined the company before 15 of the months.<br>
14. Display those employees who has joined before 15th of the month.<br>
15. Display those employees whose joining DATE is available in deptno.
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">7</td>
<td valign="top">
1. Compute the no. of days remaining in this year.<br>
2. Find the highest and lowest salaries and the difference between of them.<br>
3. List employee whose commission is greater than 25 % of their salaries.<br>
4. Make a query that displays salary in dollar format.<br>
5. Create a matrix query to display the job, the salary for that job based on department number, and the total salary for that job for all departments, giving each column an appropriate heading.<br>
6. Query that will display the total no of employees, and of that total the number who were hired in 1980,1981,1982 and 1983. Give appropriate column heading.<br>
7. Query to get the last Sunday of Any Month.<br>
8. Display department numbers and total number of employees working in each department.<br>
9. Display the various jobs and total number of employees within each job group.<br>
10. Display the depart numbers and total salary for each department.
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">8</td>
<td valign="top">
<strong>Perform the following Query</strong><br>
1. Display all employees with their dept name.<br>
2. Display those employees whose manager names is jones, and also display their manager name.<br>
3. Display employee name, his job, his dept name, his manager name, his grade and make out of an under department wise.<br>
4. List out all the employees name, job, and salary grade and department name for everyone in the company except ‘clerk’. Sort on salary display the highest salary.<br>
5. Display employee name, his job and his manager. Display also employees who are without manager.<br>
6. List the employee name, job, annual salary, deptno, dept name and grade who earn 36000 a year or who are not clerks.<br>
7. List ename, job, annual sal, deptno, dname and grade who earn 30000 per year and who are not clerks.<br>
8. List out all employees by name and number along with their manager’s name and number also display ‘no manager’ who has no manager.<br>
9. Select dept name, dept no and sum of sal.<br>
10. Display employee number, name and location of the department in which he is working.<br>
11. Display employee name and department name for each employee.
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">9</td>
<td valign="top">
1. Display the name of emp name who earns highest salary.<br>
2. Display the employee number and name of employee working as clerk and earning highest salary among clerks.<br>
3. Display the names of the salesman who earns a salary more than the highest salary of any clerk.<br>
4. Display the names of clerks who earn salary more than that of james of that of sal lesser than that of scott.<br>
5. Display the names of employees who earn a sal more than that of james or that of salary greater than that of scott.<br>
6. Display the names of the employees who earn highest salary in their respective departments.<br>
7. Display the names of employees who earn highest salaries in their respective job groups.<br>
8. Display the employee names who are working in accounting dept.<br>
9. Display the employee names who are working in chicago.<br>
10. Display the job groups having total salary greater than the maximum salary for managers.
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">10</td>
<td valign="top">
1. Display the names of employees from department number 10 with salary greater than that of any employee working in other departments.<br>
2. Display the names of employee from department number 10 with salary greater than that of all employee working in other departments.<br>
3. Display the details of employees who are in sales dept and grade is 3.<br>
4. Display those who are not managers and who are managers anyone.<br>
5. Display those employees whose manager name is jones.<br>
6. Display ename who are working in sales dept.<br>
7. Display employee name, deptname, salary and comm. For those sal in between 2000 to 5000 while location is chicago.<br>
8. Display those employees whose salary greater than his manager salary.<br>
9. Display those employees who are working in the same dept where his manager is working.<br>
10. Display grade and employees name for the dept no 10 or 30 but grade is not 4, while joined the company before 31-dec-82.
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">11</td>
<td valign="top">
1. Delete those employees who joined the company before 31-dec-82 while there dept location is ‘new york’ or ‘chicago’.<br>
2. Display employee name, job, deptname, location for all who are working as managers.<br>
3. Display name and salary of ford if his sal is equal to high sal of his grade.<br>
4. Find out the top 5 earner of company.<br>
5. Display the name of those employees who are getting highest salary.<br>
6. Display those employees whose salary is equal to average of maximum and minimum.<br>
7. Display dname where at least 3 are working and display only dname.<br>
8. Display name of those managers names whose salary is more than average salary of company.<br>
9. Display those managers name whose salary is more than an average salary of his employees.<br>
10. Display employee name, sal, comm and net pay for those employees whose net pay are greater than or equal to any other employee salary of the company?
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">12</td>
<td valign="top">
1. Display those employees whose salary is less than his manager but more than salary of any other managers.<br>
2. Find out the number of employees whose salary is greater than their manager salary?<br>
3. Display those managers who are not working under president but they are working under any other manager?<br>
4. Delete those department where no employee working?<br>
5. Delete those records from emp table whose deptno not available in dept table?<br>
6. Display those earners whose salary is out of the grade available in sal grade table?<br>
7. Display employee name, sal, comm. And whose net pay is greater than any other in the company?<br>
8. Display those employees who are working in sales or research?<br>
9. Display the grade of jones?<br>
10. Display the department name the no of characters of which is equal to no of employees in any other department?
</td>
<td valign="top" align="center">1,2</td>
</tr>
<tr>
<td valign="top" align="center">13</td>
<td valign="top">
Study & Implementation of Rollback, Commit, Savepoint.
</td>
<td valign="top" align="center">1,2,3</td>
</tr>
<tr>
<td valign="top" align="center">14</td>
<td valign="top">
Creating Database /Table Space<br>
• Managing Users: Create User, Delete User<br>
• Managing roles:-Grant, Revoke.
</td>
<td valign="top" align="center">1,2,3</td>
</tr>
<tr>
<td valign="top" align="center">15</td>
<td valign="top">
Study & Implementation of Database Backup & Recovery commands.
</td>
<td valign="top" align="center">1,2,3</td>
</tr>
</tbody>
</table>
</div>
