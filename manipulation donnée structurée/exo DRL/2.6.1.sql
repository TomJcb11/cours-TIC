select c.course_name, p.professor_name, section_name
from dbo.course as c 
join dbo.professor as p on c.professor_id = p.professor_id
join dbo.section as s on p.section_id = s.section_id
order by course_name
