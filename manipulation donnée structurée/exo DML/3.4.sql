insert into student(student_id,first_name,last_name,birth_date,section_id,year_result,course_id)
values (28,'Chuck','Norris','1940-03-10',
	(select section_id from student where last_name like 'Reeves'),
	8,'EG'+ RIGHT((select course_id
					from course c1 JOIN professor p 
					on c1.professor_id = p.professor_id
					where p.professor_name like 'Zidda'),4))