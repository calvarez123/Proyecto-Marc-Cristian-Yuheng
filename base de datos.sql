drop database if exists CHOOSE_ADVENTURE;
create database if not exists CHOOSE_ADVENTURE;
use CHOOSE_ADVENTURE;
create table if not exists USER (
id_user int primary key,
username varchar(100) ,
password varchar(100),
user_create varchar (100),
user_modifications varchar (100),
data_creation date,
user_modification date
);
create table if not exists CHARACTERS (
id_character int primary key,
name varchar(100) ,
description varchar(100),
user_create varchar (100),
user_modifications varchar (100),
data_creation date,
user_modification date
);
create table if not exists ADVENTURES (
id_adventures int unsigned auto_increment primary key,
name varchar (100) ,
description varchar(100),
user_create varchar (100),
user_modifications varchar (100),
data_creation date,
user_modification date
);
create table if not exists GAME (
id_game int primary key,
id_user int ,
id_characters int ,
desicions varchar(100) ,
id_adventures int ,
data timestamp,
user_create varchar (100),
user_modifications varchar (100),
data_creation date,
user_modification date
);
create table if not exists STEPS (
id_step int  primary key,
description varchar(100) ,
final_step bit (1),
id_adventure int,
user_create varchar (100),
user_modifications varchar (100),
data_creation date,
user_modification date
);
create table if not exists OPTIONS (
id_option int unsigned auto_increment primary key,
description varchar(100),
answer varchar(100),
id_step int,
user_create varchar (100),
user_modifications varchar (100),
data_creation date,
user_modification date
);
