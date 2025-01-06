update section
set delegate_id= (Select delegate_id
					from section
					where section_id = '1320'
					),
	section_name=(Select section_name
					from section 
					where section_id = '1320'
					)
where section_id= 1530