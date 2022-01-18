use CHOOSE_ADVENTURE;
#user
alter table USER modify id_user int unsigned auto_increment primary key;
alter table USER modify username varchar(100) not null unique;
alter table USER modify password varchar(100) not null;
#characters
alter table CHARACTERS modify id_character int unsigned auto_increment primary key;
alter table CHARACTERS modify name varchar(100) not null;
alter table CHARACTERS modify description varchar(100) not null;
#Adventures
alter table ADVENTURES modify id_adventures int unsigned auto_increment primary key;
alter table ADVENTURES modify name varchar (100) not null unique;
alter table ADVENTURES modify description varchar (100) not null unique;
#Games
alter table GAMES modify id_game int unsigned auto_increment primary key;
alter table GAMES modify id_user int unsigned;
alter table GAMES modify id_characters int unsigned;
alter table GAMES modify desicions varchar(100) not null;
alter table GAMES modify id_adventures int unsigned;
alter table GAMES constraint fk_game_user foreign key (id_user) references USER(id_user), 
#steps
alter table STEPS modify id_step int unsigned auto_increment primary key;
alter table STEPS modify description varchar(100) not null;
alter table STEPS modify final_step boolean;
alter table STEPS modify id_adventure int unsigned;
#options
alter table OPTIONS modify id_option int unsigned auto_increment primary key;
alter table OPTIONS modify description varchar(100) not null;
alter table OPTIONS modify answer varchar(100) not null;
alter table OPTIONS modify id_step int unsigned;
