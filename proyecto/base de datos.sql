drop database if exists CHOOSE_ADVENTURE;
create database if not exists CHOOSE_ADVENTURE;
use CHOOSE_ADVENTURE;
create table if not exists USER (
id_user int unsigned auto_increment primary key,
username varchar(100) not null unique,
password varchar(100) not null
);
create table if not exists CHARACTERS (
id_character int unsigned auto_increment primary key,
name varchar(100) not null,
description varchar(100) not null
);
create table if not exists ADVENTURES (
id_adventures int unsigned auto_increment primary key,
name varchar (100) not null unique,
description varchar(100) not null
);
create table if not exists GAME (
id_game int unsigned auto_increment primary key,
id_user int unsigned,
id_characters int unsigned,
desicions varchar(100) not null,
id_adventures int unsigned,
data timestamp,
constraint fk_game_user foreign key (id_user) references USER(id_user),
constraint fk_game_characters foreign key (id_characters) references CHARACTERS(id_character),
constraint fk_game_adventures foreign key (id_adventures) references ADVENTURES(id_adventures)
);
create table if not exists STEPS (
id_step int unsigned auto_increment primary key,
description varchar(100) not null,
final_step boolean,
id_adventure int unsigned,
constraint fk_steps_adventure foreign key (id_adventure) references ADVENTURES(id_adventures)
);
create table if not exists OPTIONS (
id_option int unsigned auto_increment primary key,
description varchar(100) not null,
answer varchar(100) not null,
id_step int unsigned,
constraint fk_options_steps foreign key (id_step) references STEPS(id_step)
);
