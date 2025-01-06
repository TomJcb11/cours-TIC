select p.professor_id, sum(course_ects) as total_ECTS
from dbo.professor as p 
left join dbo.course as c  on p.professor_id = c.professor_id

group by p.professor_id
order by total_ECTS desc 