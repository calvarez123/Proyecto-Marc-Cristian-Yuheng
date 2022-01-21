use CHOOSE_ADVENTURE;
#user
alter table USER modify id_user int unsigned auto_increment ;
alter table USER modify username varchar(100) not null unique;
alter table USER modify password varchar(100) not null;
alter table USER modify user_create varchar(100)  null;
alter table USER modify user_modifications varchar(100)  null;
alter table USER modify data_creation date  null;
alter table USER modify user_modification date  null;
#characters
alter table CHARACTERS modify id_character int unsigned auto_increment ;
alter table CHARACTERS modify name varchar(500) not null;
alter table CHARACTERS modify description varchar(500) not null;
alter table CHARACTERS  modify user_create varchar(100)  null;
alter table CHARACTERS  modify user_modifications varchar(100)  null;
alter table CHARACTERS  modify data_creation date  null;
alter table CHARACTERS  modify user_modification date  null;
#Adventures
alter table ADVENTURES modify id_adventures int unsigned auto_increment ;
alter table ADVENTURES modify name varchar (100) not null unique;
alter table ADVENTURES modify description varchar (500) not null unique;
alter table ADVENTURES modify user_create varchar(100)  null;
alter table ADVENTURES modify user_modifications varchar(100)  null;
alter table ADVENTURES modify data_creation date  null;
alter table ADVENTURES modify user_modification date  null;
#Games
alter table GAME modify id_game int unsigned auto_increment ;
alter table GAME modify id_user int unsigned;
alter table GAME modify id_characters int unsigned;
alter table GAME modify desicions varchar(500) not null;
alter table GAME modify id_adventures int unsigned;
alter table GAME modify user_create varchar(100)  null;
alter table GAME modify user_modifications varchar(100)  null;
alter table GAME modify data_creation date  null;
alter table GAME modify user_modification date  null;
alter table GAME add constraint fk_game_user foreign key (id_user) references USER(id_user); 
alter table GAME add constraint fk_game_characters foreign key (id_characters) references CHARACTERS(id_character) ; 
alter table GAME add constraint fk_game_adventures foreign key (id_adventures) references ADVENTURES(id_adventures); 
#steps
alter table STEPS modify id_step int unsigned auto_increment ;
alter table STEPS modify description varchar(500) not null;
alter table STEPS modify final_step bit (1);
alter table STEPS modify id_adventure int unsigned;
alter table STEPS modify user_create varchar(100)  null;
alter table STEPS modify user_modifications varchar(100)  null;
alter table STEPS modify data_creation date  null;
alter table STEPS modify user_modification date  null;
alter table STEPS add constraint fk_steps_adventure foreign key (id_adventure) references ADVENTURES(id_adventures);
#options
alter table OPTIONS modify id_option int unsigned auto_increment ;
alter table OPTIONS modify description varchar(500) not null;
alter table OPTIONS modify answer varchar(500) not null;
alter table OPTIONS modify id_step int unsigned;
alter table OPTIONS modify user_create varchar(100)  null;
alter table OPTIONS modify user_modifications varchar(100)  null;
alter table OPTIONS modify data_creation date  null;
alter table OPTIONS modify user_modification date  null;
alter table OPTIONS add constraint fk_options_steps foreign key (id_step) references STEPS(id_step)
