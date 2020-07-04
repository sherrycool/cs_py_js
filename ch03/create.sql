create table flights (
	id serial primary key,
	origin varchar(50) not null,
	destination varchar(50) not null,
	duration int not null
);


insert into flights (origin, destination, duration) values ('New York', 'London', 415);
insert into flights (origin, destination, duration) values ('Shanghai', 'Paris', 760);
insert into flights (origin, destination, duration) values ('Istanbul', 'Tokyo', 700);
insert into flights (origin, destination, duration) values ('New York', 'Paris', 435);
insert into flights (origin, destination, duration) values ('Moscow', 'Paris', 245);
insert into flights (origin, destination, duration) values ('Lima', 'New York', 455);


create table passengers (
	id serial primary key,
	name varchar(50) not null,
	flight_id int not null /*应该是外键 但是报错*/
);

insert into passengers (name, flight_id) values ('Alice', 1);
insert into passengers (name, flight_id) values ('Bob', 1);
insert into passengers (name, flight_id) values ('Charlie', 2);
insert into passengers (name, flight_id) values ('Dava', 2);
insert into passengers (name, flight_id) values ('Erin', 4);
insert into passengers (name, flight_id) values ('Frank', 6);
insert into passengers (name, flight_id) values ('Grace', 6);