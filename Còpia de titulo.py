#Connectar al BBDD
import pymysql
class DataBase:
    def _init_(self):
        self.connection = pymysql.connect()

#Connectar al BBDD


totalusers={1:['pepemanolo','S232dwd---',True],2:['papajorge','Sd232---23',True],3:['manolito','d33--DDDe',True]}
login=False

def menunologin():
    error = True
    while error== True:
        figura=('''
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
''')#figura
        print(figura)
        menu = '1) Login\n2) Create user\n3) Replay Adventure\n4) Reports\n5) Exit '.split('\n')
        for i in menu:
            print(' ' * 65, i)
        opc=input('-->Option:')
        if opc == '1' or opc == '2' or opc == '3' or opc == '4' or opc == '5':
            return opc
        else:
            input('**********Invalid option**********\n\n Press enter to continue')

            error= True


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

    if opc == '1':
        login2='logout'
        return login2

    elif opc == '2':
        print('='*50,'Adventures','='*50)

    elif opc == '3':
        print('opcion 3')
    elif opc == '4':
        print('opcion 4')
    elif opc == '5':
        print(232)
        exit1='exit'
        return exit1


def menu_options(opc):

    if opc == '1':
        validation = False
        while validation == False:
            username = input('USERNAME: ')
            pasos = 0
            for i in totalusers :
                if username==totalusers[i][0]:
                    validation=True
                    break
            if validation==False:
                print("USERNAME not found")

        validation1 = False
        while validation1 == False:
            password = input('PASSWORD: ')
            if password == totalusers[i][1]:
                validation1 = True
                salir=True
                break
            if validation1 == False:
                print("Password not correct")

        if salir == True:
            print("USER LOGED")
            input("Press ENTER to continue")
            user = [username, password, True]

            return user

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
                    salir = True
                else:
                    print("PASSWORD has to contain mayus and minus ")
                    validation1 = False
                    validation2 = False
                    validation3 = False
                    validation4 = False
                    break
            if salir == True:
                print("USER CREATED")
                input("Press ENTER to continue")
                user=[username,password,True]

                return user

    elif opc == '3':
        print('opcion 3')
    elif opc == '4':
        print('opcion 4')
    elif opc == '5':
        print(232)
        exit1='exit'
        return exit1



while True:
    login1=menu_options(menunologin())

    if login1=='exit':
        print("BYE")
        break

    if login1[2]==True:
        totalusers[len(totalusers)+1]=login1
        print(totalusers)
        login2=menu_options_loged(menuloged())
        if login2=='logout':
            print('Press ENTER to continue')
            input()
        elif login2=='salir':
            login1='exit'
