use CHOOSE_ADVENTURE;
                                                #historia 1
insert into ADVENTURES (
name,description) value ('Cobra kai','En esta historia lucharemos como un crobra kai, un dojo de karate moderno que tiene como reglas principales
Pegar primero, Pegar duro, Sin piedad. Estaremos en un combate de uno contro contra el ganador del torneo Daniel LaRusso y tendremos que escoger que movimientos hacer y 
hacia que lados atacar para ganar el combate y hacerle frente al campeon nacional de karate');
#personajes
insert into CHARACTERS (name, description) value ('kratos','Es un guerrero griego muy poderoso, es el asesino de Zeus y todos los dioses de grecia, a dia de hoy est luchando contra los dioses nordicos.');
insert into CHARACTERS (name, description) value ('cristiano ronaldo','Es un jugador de futbol poco conocido, tiene mucha fuerza en las piernas y esta muy fuerte, es habil en muchas habilidades fisicas pero mentales no tanto.');
insert into CHARACTERS (name, description) value ('ibai','Es el streammer mas famoso de habla hispana, es muy gracioso, y muy inteligente, pero a nivel fisico deja mucho que desear.');
#pasos 1
insert into STEPS (description) value ('Daniel LaRusso te a retado a un combate, que decides hacer?');
insert into STEPS (description) value ('Daniel LaRusso te a pegado una patada voladora en la cara, si resibes muchas caeras KO que decides hacer?');
insert into STEPS (description) value ('Daniel LaRusso se tambalea por el ostion que le has pegado, es tu momento de ganar el combate, que decides hacer');
insert into STEPS (description, final_step) value ('Daniel LaRusso ha caido inconciente en el suelo, Has ganado el combate!!!',1);
insert into STEPS (description, final_step) value ('Daniel LaRusso te ha pegado un puñetazo doble en la cara y a acabado contigo.',1);
#opciones 1
insert into OPTIONS (description, answer) value ('le pegas un puñetazo en la cara y comienzas el combate','Daniel LaRusso ha recibito tu ataque directo, se a enfadado muchisimo');
insert into OPTIONS (description, answer) value ('decides irte y no hacerle caso a el gran Daniel LaRusso','Sales corriendo pero te caes y hace que tu enemigo te enganche en el suelo y siga la batalla');
insert into OPTIONS (description, answer) value ('Le pides perdon e intentas que no se forme ninguna pelea','Le pides perdon pero a el le da igual, solo quiere reventarte');
#opciones 2
insert into OPTIONS (description, answer) value ('Decides protegerte de su siguiente ataque ya que es muy fuerte','Logras protegerte de su ataque, el ya esta cansado, podria ser hora de atacarle');
insert into OPTIONS (description, answer) value ('Intentas esquivar sus ataques y darle un puñetezo en cuanto falle un golpe','Daniel no falla nunca, pero consigues desviar uno de sus ataques y ponerte en guardia');
insert into OPTIONS (description, answer) value ('Sales corriendo y evitas la pelea','Ese puñetazo hace que se ponga a llorar y ganas la batalla');
#opciones 3
insert into OPTIONS (description, answer) value ('Esquivas su golpe y sales corriendo y gritando que llamen a la policia','un vecino de la zona llama a la policia y te libras de su paliza');
insert into OPTIONS (description, answer) value ('Le pegas una patada en la cara','Le pegas la patada y logras tirarlo al suelo');
insert into OPTIONS (description, answer) value ('Le pegas un puñetazo en el estomago','Ese puñetazo hace que se ponga a llorar y ganas la batalla');

                                                 #historia 2
insert into ADVENTURES (name,description) value ('Lucha contra duendes','Ya es la hora, héroe de nuestra patria, vosotros representáis el futuro de los humanos, 
luchad por lo que quereis, luchad por vuestra patria!!!’’. Te han obligado a alistarse en el ejército por la guerra que ha provocado los humanos a los 
duendes por conquistas de tierras, sigue los órdenes del comandante o intenta sobrevivir.');