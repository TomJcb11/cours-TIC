update student
set year_result = '18',
	last_name = 'Crowe',
	login = LOWER(LEFT((Select first_name from student where student_id=27),1)
			+''+
			(select last_name from student where student_id=27))
	where student_id=27