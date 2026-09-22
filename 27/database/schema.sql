CREATE DATABASE IF NOT EXISTS book_keeping;
USE book_keeping;


CREATE TABLE IF NOT EXISTS users
(
    id int auto_increment primary key,
    name varchar(128) not null,
    dob  date not null,
    email varchar(128) not null
);

CREATE TABLE IF NOT EXISTS payments
(
    id int auto_increment primary key,
    user_id int not null,
    amount decimal(10, 2) not null,
    created_at date not null,
    constraint payments__user__id__fk
        foreign key (user_id) references users (id)
);

