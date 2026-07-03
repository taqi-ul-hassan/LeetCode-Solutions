# Write your MySQL query statement belowU
UPDATE Salary
SET sex = CASE
when sex = 'm' THEN  'f'
when sex = 'f' THEN 'm'
END;