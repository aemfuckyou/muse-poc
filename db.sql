create schema if not exists muse;
drop table if exists muse.raw_data;
drop table if exists muse.tests;
drop table if exists muse.test_type;
drop table if exists muse.user_data;


-- check tables in muse schema
select *
from pg_catalog.pg_tables
where schemaname = 'muse';


create table muse.user_data (
	user_id serial primary key,
	user_name text not null unique
);

create table muse.test_type(
	type_id int primary key,
	type_name text not null
);

create table muse.tests (
	test_id serial primary key,
	user_id int, --foreign key
	test_type_id int, --foreign key
	start_time timestamp not null,
	end_time timestamp,
	interrupt bool,
	constraint fk_user_tests foreign key(user_id) references muse.user_data(user_id),
	constraint fk_type_tests foreign key(test_type_id) references muse.test_type(type_id)
);

create table muse.raw_data (
	raw_data_id serial primary key,
	test_id int, --foreign key
	raw_time_stamp timestamp not null,
	TP9 float8 not null,
	AF7 float8 not null,
	AF8 float8 not null,
	TP10 float8 not null,
	AUXR float8 not null,
	constraint fk_test_raw foreign key(test_id) references muse.tests(test_id)
);


insert into muse.test_type (type_id, type_name) values (1, 'visual'),(2,'audio_visual');

select count(*), d.test_id from muse.raw_data d group by d.test_id;

