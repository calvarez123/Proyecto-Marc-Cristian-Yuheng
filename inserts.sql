use CHOOSE_ADVENTURE;
                                                #historia 1
insert into ADVENTURES (
name,description) value ('Cobra kai','En esta historia lucharemos como un crobra kai, un dojo de karate moderno que tiene como reglas principales Pegar primero, Pegar duro, Sin piedad. Estaremos en un combate de uno contro contra el ganador del torneo Daniel LaRusso y tendremos que escoger que movimientos hacer y hacia que lados atacar para ganar el combate y hacerle frente al campeon nacional de karate');
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
insert into ADVENTURES (name,description) value ('Lucha contra duendes','Ya es la hora, héroe de nuestra patria, vosotros representáis el futuro de los humanos, luchad por lo que quereis, luchad por vuestra patria!!!’’. Te han obligado a alistarse en el ejército por la guerra que ha provocado los humanos a los duendes por conquistas de tierras, sigue los órdenes del comandante o intenta sobrevivir.');
#pasos

insert into STEPS (description) value ('Durante la lucha contra los duendes has visto que todos los duendes tienen escudos y espadas de madera o piedra, mientras que todos vosotros teneis armaduras de acero');
insert into STEPS (description) value ('has visto un dominio de magia oscura donde invoco un brujo duende antes de morir, y ahi sale un ejercito lleno de demonios inmortales:');
#opciones 1
insert into OPTIONS (description, answer) value ('Atacar primero y animar el equipo a la conquista ', 'Lograstes ganar la guerra contra los duendes. pero...');
insert into OPTIONS (description, answer) value ('Seguir detras del equipo y intentar evitar lucha:', 'Tu comportamiento esta en ojo del comandante no tienes otra opcion de luchar ya que si no lo haces se pondra en duda tu lealtad a la corona');
insert into OPTIONS (description, answer) value ('Esperas y planeas otra forma de atacar al ejercito enemigo y asi salir victorioso sin tantas bajas', 'Sin darte cuenta el ejercito de duendes os rodea y os empieza a atacar por la espalda, lo que hace que pierdas la batalla y resultes gravemente herido');
#opciones 2
insert into OPTIONS (description, answer) value ('Decides luchar contra ellos ya que estas en racha y no tienes en mente perder. ', 'No eres enemigo de ellos te mato en seguida, pero despues de un tiempo vino un fantasma que te sobrevivio, haciendo que se desaparezca el, y conseguistes el poder de reencarnación a los muertos que luchen por ti.');
insert into OPTIONS (description, answer) value ('Intentar escapar del dominio magico lo mas rapido posible ya que no vas a poder ganarles nunca.', 'El dominio enemigo tiene una pared de magia que te quema a ti y a todas tus tropas por completo perdidendo asi la lucha.');
insert into OPTIONS (description, answer) value ('Decides atacar por la espalda del enemigo, de una manera mas estrategica y con cabeza', 'Logras destruir a las tropas del enemigo pero queda luchar contra un gigante verde que te asesina pero consigues ganar la guerra.');
#opciones 3
insert into OPTIONS (description, answer) value ('Decides luchar en contra ellos ya que estas en racha y no tienes en mente perder. ', 'No eres enemigo de ellos te mato en seguida, pero despues de un tiempo vino un fantasma que te sobrevivio, haciendo que se desaparezca el, y conseguistes el poder de reencarnación a los muertos que luchen por ti.');
insert into GAME (desicions) value ('partida numero 1');

                                                 #historia 3
insert into ADVENTURES (name,description) value ('Muertos vivientes','Despues de la obtencion del poder, sigues caminando a la vuelta del bosque para volver a casa, pero los demonios tambien han pasado por aqui, y han arruinado todo el bosque y matando a los elfos que estan viviendo alli, y la magia oscura esta en todas partes,tienes que ir con cuidado');
#pasos 1
insert into STEPS (description) value ('Cuando ibas andando una mano te cogio, es de un elfo herido te pide que le lleves a su laboratorio, para intentar curarse de las heridas');
#opciones 1
insert into OPTIONS (description, answer) value ('Decides llevarle al laboratorio','Cuando le llevas al laboratorio, la mayoria de los hechizos que tenia ya han sido devorados por la magia oscura, pero te dice que con un petalo de la flor de la amanecer, podria purificarlos, te pide que vayas al sud del bosque a buscar, pero mientras tanto has visto unos equipamientos hechizados que ha podido resistir a la devoracion del hechizo.');
insert into OPTIONS (description, answer) value ('Decides llevarle al laboratorio','Cuando le llevas al laboratorio, la mayoria de los hechizos que tenia ya han sido devorados por la magia oscura, pero te dice que con un petalo de la flor de la amanecer, podria purificarlos, te pide que vayas al sud del bosque a buscar, pero mientras tanto has visto unos equipamientos hechizados que ha podido resistir a la devoracion del hechizo.');







