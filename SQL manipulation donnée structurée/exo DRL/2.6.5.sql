select last_name, year_result, grade
from dbo.student as s 
join dbo.grade as g on s.year_result between g.lower_bound and g.upper_bound
where year_result >= 12
order by grade asc