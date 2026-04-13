-- Write your SQL query here
select emp.name, emp.salary, dept.dept_name
from employees emp inner join departments dept on emp.dept_id = dept.id
order by emp.name asc;