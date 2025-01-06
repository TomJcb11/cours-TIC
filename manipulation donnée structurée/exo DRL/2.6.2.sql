select sec.section_id, section_name, last_name
from dbo.section as sec
join dbo.student as stu on sec.delegate_id = stu.student_id


order by section_id desc