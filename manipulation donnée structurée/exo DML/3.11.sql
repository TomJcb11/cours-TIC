update section
set section.delegate_id = student.student_id
from section join student
	on section.section_id = student.section_id
where student.last_name LIKE 'Milano'