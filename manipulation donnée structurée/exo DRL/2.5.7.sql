select course_id,section_id, avg(CONVERT(float,year_result)) as Moyenne
from student

where section_id in (1010,1320)

group by cube( course_id,section_id)

