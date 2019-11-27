create table "user"
(
    id   serial not null
        constraint user_pk
            primary key,
    name varchar(20),
    age  integer
);

alter table "user"
    owner to postgres;

insert into "user" values (1, 'sam', 19), (2, '阿坤', 20);
