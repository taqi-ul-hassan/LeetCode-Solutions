# Write your MySQL query statement below
select m.name as Employee from Employee as m
join Employee as e on e.id = m.managerId
where m.salary > e.salary;