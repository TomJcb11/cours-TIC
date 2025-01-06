select section_id, course_id, avg(CONVERT(float,year_result)) as Moyenne
from student

where section_id in (1010,1320)

group by rollup(section_id, course_id)