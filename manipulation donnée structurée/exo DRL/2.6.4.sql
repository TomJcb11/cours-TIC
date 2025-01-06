select s.section_id ,section_name, professor_name
from dbo.section as s
 join dbo.professor as p on s.section_id = p.section_id
order by s.section_id desc