# Write your MySQL query statement below
select u.name as NAME, sum(t.amount) as BALANCE from Users as u 
inner join Transactions as t on u.account = t.account
group by t.account having balance > 10000;