update section
set delegate_id = (Select student_id
					from student
					where first_name = 'Keanu'
					AND last_name = 'Reeves')
Where section_id = 1530