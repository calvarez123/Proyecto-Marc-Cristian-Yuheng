from importlib import import_module
from re import T
import pymysql
import getUser

conn = pymysql.connect(host='52.148.209.79', user='cym', password='password', db='CHOOSE_ADVENTURE')
cur = conn.cursor()
# descript de
query = "select description from ADVENTURES where id_adventures='2'"
cur.execute(query)
descripcion = cur.fetchall()
#print(descripcion[0][0])

login = False
login1=['None','None',False]

query='select * from CHARACTERS'
cur.execute(query)
rows=cur.fetchall()
print(rows)

def menunologin():
    error = True
    while error == True:
        figura = ('''
**********************************************************************************************************************************************************
                                                ######  ######  ######  #######  ########  ######  
                                                ######  ######  ######  #######  ########  ######
                                                ##      ##      ##      ##   ##  ##        ##
                                                ##      ##      ##      ##   ##  ##        ##
                                                ######  ######  ##      ##   ##  ##        ######
                                                ######  ######  ##      ##   ##  ## #####  ######
                                                ##          ##  ##      ##   ##  ## #####  ##
                                                ##          ##  ##      ##   ##  ##    ##  ##
                                                ######  ######  ######  #######  ########  ######
                                                ######  ######  ######  #######  ########  ###### 

                                                                ##########  ##   ##
                                                                ##########  ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      #######
                                                                    ##      #######

                                    ########  ##      ##  ######  ###     ##  ########  ##   ##  ####     ########
                                    ########  ##      ##  ######  ###     ##  ########  ##   ##  #####    ########
                                    ##    ##  ##      ##  ##      ## ##   ##     ##     ##   ##  ##  ##   ##    ##
                                    ##    ##  ##      ##  ##      ## ##   ##     ##     ##   ##  ##   ##  ##    ##
                                    ########   ##    ##   ######  ##  ##  ##     ##     ##   ##  ##   ##  ########
                                    ########   ##    ##   ######  ##  ##  ##     ##     ##   ##  ######   ########
                                    ##    ##   ##    ##   ##      ##   ## ##     ##     ##   ##  #####    ##    ##
                                    ##    ##    ##  ##    ##      ##   ## ##     ##     ##   ##  ## ##    ##    ##
                                    ##    ##    ######    ######  ##    ####     ##     #######  ##  ##   ##    ##
                                    ##    ##     ####     ######  ##    ####     ##     #######  ##   ##  ##    ##
**********************************************************************************************************************************************************
''')  # figura
        print(figura)
        menu = '1) Login\n2) Create user\n3) Replay Adventure\n4) Reports\n5) Exit '.split('\n')
        for i in menu:
            print(' ' * 65, i)
        opc = input('-->Option:')
        if opc == '1' or opc == '2' or opc == '3' or opc == '4' or opc == '5':
            return opc
        else:
            input('**********Invalid option**********\n\n Press enter to continue')

            error = True


def menuloged():
    error = True
    while error == True:
        figura = ('''
**********************************************************************************************************************************************************
                                                ######  ######  ######  #######  ########  ######  
                                                ######  ######  ######  #######  ########  ######
                                                ##      ##      ##      ##   ##  ##        ##
                                                ##      ##      ##      ##   ##  ##        ##
                                                ######  ######  ##      ##   ##  ##        ######
                                                ######  ######  ##      ##   ##  ## #####  ######
                                                ##          ##  ##      ##   ##  ## #####  ##
                                                ##          ##  ##      ##   ##  ##    ##  ##
                                                ######  ######  ######  #######  ########  ######
                                                ######  ######  ######  #######  ########  ###### 

                                                                ##########  ##   ##
                                                                ##########  ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      #######
                                                                    ##      #######

                                    ########  ##      ##  ######  ###     ##  ########  ##   ##  ####     ########
                                    ########  ##      ##  ######  ###     ##  ########  ##   ##  #####    ########
                                    ##    ##  ##      ##  ##      ## ##   ##     ##     ##   ##  ##  ##   ##    ##
                                    ##    ##  ##      ##  ##      ## ##   ##     ##     ##   ##  ##   ##  ##    ##
                                    ########   ##    ##   ######  ##  ##  ##     ##     ##   ##  ##   ##  ########
                                    ########   ##    ##   ######  ##  ##  ##     ##     ##   ##  ######   ########
                                    ##    ##   ##    ##   ##      ##   ## ##     ##     ##   ##  #####    ##    ##
                                    ##    ##    ##  ##    ##      ##   ## ##     ##     ##   ##  ## ##    ##    ##
                                    ##    ##    ######    ######  ##    ####     ##     #######  ##  ##   ##    ##
                                    ##    ##     ####     ######  ##    ####     ##     #######  ##   ##  ##    ##
**********************************************************************************************************************************************************
''')  # figura
        print(figura)
        menu = '1) Logout\n2) Play\n3) Replay Adventure\n4) Reports\n5) Exit '.split('\n')
        for i in menu:
            print(' ' * 65, i)
        opc = input('-->Option:')
        if opc == '1' or opc == '2' or opc == '3' or opc == '4' or opc == '5':
            return opc
        else:
            input('**********Invalid option**********\n\n Press enter to continue')

            error = True


def menu_options_loged(opc):
    while True:
        if opc == '1':
            print('See you soon',login1[0])
            input('**********Logout Succesful**********\n\n Press any key to continue')
            login2 = 'logout'
            return login2

        elif opc == '2':
            while True:
                print('Hello ', login1[0], 'lets play!!')
                print('=' * 70, 'Adventures', '=' * 70)
                print()
                print('Id Adventure       ', 'Adventure', ' ' * 40, 'Description')
                print('*' * 152)
                # adventure1
                print()
                print('1', ' ' * 17, 'Lucha contra duendes', ' ' * 29,
                      '"Ya es la hora, héroe de nuestra patria, vosotros representáis el futuro de los ')
                print(' ' * 70, 'humanos, luchad por lo que quereis, luchad por vuestra patria!!!". Te han ')
                print(' ' * 70, 'obligado a alistarse en el ejército por la guerra que ha provocado los humanos')
                print(' ' * 70, 'a los duendes por conquistas de tierras, sigue los órdenes del comandante o ')
                print(' ' * 70, 'intenta sobrevivir.')
                # adventure1
                # adventure2
                print()
                print('2', ' ' * 17, 'Muertos vivientes', ' ' * 32,
                      'Despues de la obtencion del poder, sigues caminando a la vuelta del bosque para')
                print(' ' * 70, 'volver a casa, pero los demonios tambien han pasado por aqui, y han arruinado ')
                print(' ' * 70, 'todo el bosque y matando a los elfos que estan viviendo alli, y la magia oscura ')
                print(' ' * 70, 'esta en todas partes, tienes que ir con cuidado.')
                # adventure2
                # adventure3
                print()
                print('3', ' ' * 17, 'Caza final', ' ' * 39,
                      'Un real caza contra el jefe final el Democratius, el rey de los demonios, tienes')
                print(' ' * 69, ' todas las habilidades que aprendistes en en las aventuras anteriores, vamos ')
                print(' ' * 70, 'podras hacerlo.')
                # adventure3
                whichplay = input("Choose a adventure to play(0 to go back)")
                if whichplay == '0':
                    opc = menuloged()
                    break
                elif whichplay == '1':
                    print('=' * 70, 'Characters', '=' * 70)
                    print('1) Kristoffer')
                    print('2) Eivind')
                    choose_character = input('Choose a Character')
                    if int(choose_character) == 1 or int(choose_character) == 2:
                        print()
                        print('=' * 150)
                        print('Lucha contra duendes')
                        print('=' * 150)
                        print()
                        while True:
                            print(
                                'Durante la lucha contra los duendes has visto que todos los duendes tienen escudos y espadas de madera o piedra, mientras que todos vosotros teneis \narmaduras de acero:\n ')
                            choose1 = input(
                                '1)Atacar primero y animar el equipo a la conquista:\n2)Seguir detras del equipo y intentar evitar lucha:')
                            if choose1.isdigit() == False or int(choose1) < 1 or int(choose1) > 2:
                                input('**********Invalid option**********\n\n Press enter to continue')
                            else:

                                if int(choose1) == 1:
                                    while True:
                                        print()
                                        print(
                                            'Lograstes ganar la guerra contra los duendes pero has visto un dominio de magia oscura donde invoco un brujo duende antes de morir, y ahi sale un \nejercito lleno de demonios inmortales:')
                                        choose2 = input(
                                            '1)Luchar contra ellos ya que estas en racha:\n2)Intentar escapar del dominio magico:')
                                        if choose2.isdigit() == False or int(choose1) < 1 or int(choose1) > 2:
                                            input('**********Invalid option**********\n\n Press enter to continue')
                                        else:
                                            if int(choose2) == 1:
                                                print('=' * 150)
                                                print(
                                                    'No eres enemigo de ellos te mato en seguida, pero despues de un tiempo vino un fantasma que te sobrevivio, haciendo que se desaparezca el, y \nconseguistes el poder de reencarnación a los muertos que luchen por ti.')
                                                print('FIN')
                                                print('=' * 150)
                                                exitreason = 'nivel-completado'
                                                return exitreason
                                            elif int(choose2) == 2:
                                                print('=' * 150)
                                                print(
                                                    'El dominio tiene una pared de magia que te ha quemado por completo, igualmente estas muerto')
                                                print('FIN')
                                                print('=' * 150)
                                                exitreason = 'nivel-completado'
                                                return exitreason
                                elif int(choose1) == 2:
                                    while True:
                                        print()
                                        print(
                                            'Todo tu comportamiento esta en ojo del comandante no tienes otra opcion de luchar,has visto un dominio de magia oscura donde invoco un brujo duende \nantes de morir, y ahi sale un ejercito lleno de demonios inmortales:')
                                        choose2 = input(
                                            '1)Luchar contra ellos ya que estas en racha.\n2)Intentar escapar del dominio magico:')
                                        if choose2.isdigit() == False or int(choose1) < 1 or int(choose1) > 2:
                                            input('**********Invalid option**********\n\n Press enter to continue')
                                        else:
                                            if int(choose2) == 1:
                                                print('=' * 150)
                                                print(
                                                    'No eres enemigo de ellos te mato en seguida, pero despues de un tiempo vino un fantasma que te sobrevivio, haciendo que se desaparezca el, y \nconseguistes el poder de reencarnación a los muertos que luchen por ti.')
                                                print('FIN')
                                                print('=' * 150)
                                                exitreason = 'nivel-completado'
                                                return exitreason

                                            elif int(choose2) == 2:
                                                print('=' * 150)
                                                print(
                                                    'El dominio tiene una pared de magia que te ha quemado por completo, igualmente estas muerto')
                                                print('FIN')
                                                print('=' * 150)
                                                exitreason = 'nivel-completado'
                                                return exitreason

                if whichplay != '0' or whichplay != '1' or whichplay != '2' or whichplay != '3':
                    input('**********Invalid option**********\n\n Press enter to continue')





        elif opc == '3':
            print('opcion 3')
        elif opc == '4':
            print('opcion 4')
        elif opc == '5':
            print(232)
            exit1 = 'exit'
            return exit1


def menu_options(opc):
    if opc == '1':
        while True:
            user = input('Input username: ')
            d = getUser.getUser()
            #print(d)
            for i in d:
                if user==i:
                    j = 0
                    while j < 3:
                        password = input('Input password for that username')
                        if password == d[str(user)]['password']:
                            input('**********You have entered successfully**********\n\n Press enter to continue')
                            login1 = [user, password, True]
                            return login1
                        else:
                            j = j + 1
                            if int(j) == 3:
                                print("Login failed")
                                return ['None', 'None', False]
                            print('You still have ', 3 - int(j), ' tries')

            else:
                input('**********The user is not found**********\n\n Press enter to continue')

    elif opc == '2':
        validation = False
        while validation == False:
            username = input('USERNAME: ')
            pasos = 0
            for i in username:
                pasos = pasos + 1
            if pasos > 5 and pasos < 11:
                validation = True
            else:
                print("USERNAME have to be longer than 5 and shorter than 11")
        validation1 = False
        while True:

            while validation1 == False:
                password = input('PASSWORD: ')
                pasos = 0
                for i in password:
                    pasos = pasos + 1
                if pasos > 7:
                    validation2 = False
                    validation1 = True
                else:
                    print("PASSWORD have to be longer than 7")

            while validation2 == False:
                contador = 0
                for i in password:
                    if i.isdigit() == False and i.isalpha() == False:
                        contador = contador + 1
                if contador != 0:
                    validation2 = True
                    validation3 = False
                else:
                    print("PASSWORD need to contain special character")
                    validation1 = False
                    validation3 = True
                    validation4 = True
                    validation5 = True
                    salir12=False
                    break

            while validation3 == False:
                contador = 0
                for i in password:
                    if i.isspace() == True:
                        contador = contador + 1
                if contador == 0:
                    validation3 = True
                    validation4 = False

                else:
                    print("PASSWORD cannot have spaces")
                    validation1 = False
                    validation2 = False
                    validation4 = True
                    validation5 = True
                    salir12 = False
                    break

            while validation4 == False:
                contador = 0
                for i in password:
                    if i.isdigit() == True:
                        contador = contador + 1
                if contador != 0:
                    validation4 = True
                    validation5 = False
                else:
                    print("PASSWORD has to contain numbers ")
                    validation1 = False
                    validation2 = False
                    validation3 = False
                    validation5 = True
                    break

            while validation5 == False:
                contadormayus = 0
                contadorminus = 0
                for i in password:
                    if i.isalpha() == True:
                        if i.isupper() == True:
                            contadormayus = contadormayus + 1
                        elif i.islower() == True:
                            contadorminus = contadorminus + 1
                if contadorminus != 0 and contadormayus != 0:
                    validation5 = True
                    salir12 = True
                else:
                    print("PASSWORD has to contain mayus and minus ")
                    validation1 = False
                    validation2 = False
                    validation3 = False
                    validation4 = False
                    break
            if salir12 == True:
                conn = pymysql.connect(host='52.148.209.79', user='cym', passwd='password', db='CHOOSE_ADVENTURE')
                cur = conn.cursor()
                input('**********The user is created**********\n\n Press enter to continue')
                query = "INSERT INTO USER(username,password) VALUES(%s,%s)"
                USER = (username, password)
                cur.execute(query, USER)
                conn.commit()
                login1=[username,password,True]
                return login1

    elif opc == '3':
        print('opcion 3')
    elif opc == '4':
        print('opcion 4')
    elif opc == '5':
        print(232)
        exit1 = 'exit'
        return exit1


while True:
    login1 = menu_options(menunologin())
    if login1 == 'exit':
        print("BYE")
        break
    while True:
        if login1[2] == True:
            login2 = menu_options_loged(menuloged())
            if login2 == 'logout':
                break
            elif login2 == 'nivel-completado':
                input("Press enter to continue")
            elif login2 == 'salir':
                login1 = 'exit'
