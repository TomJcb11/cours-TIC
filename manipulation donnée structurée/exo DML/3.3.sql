Create table section_archives(
	section_id_arch int primary key,
	section_name_arch varchar(50),
	delegate_id_arch int
)

insert into section_archives
	select * from section