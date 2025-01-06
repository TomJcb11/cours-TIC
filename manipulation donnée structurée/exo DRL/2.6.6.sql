select professor_name, section_name, course_name, course_ects 
from professor as p
left join section as s on p.section_id = s.section_id
left join course as c on p.professor_id = c.professor_id

order by course_ects desc

