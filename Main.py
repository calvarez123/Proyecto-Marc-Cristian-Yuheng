from importlib import import_module
from re import T
import pymysql
import getUser
import datetime

conn = pymysql.connect(host='52.148.209.79', user='cym', password='password', db='CHOOSE_ADVENTURE')
cur = conn.cursor()
# descript de
query = "select description from ADVENTURES where id_adventures='2'"
cur.execute(query)
descripcionadven1 = cur.fetchall()
query="Select name, description from ADVENTURES"
cur.execute(query)
nomhis_descpcion = cur.fetchall()
descrip_his1=nomhis_descpcion[0][1]

login = False
login1=['None','None',False]
desadven1=descripcionadven1[0][0]

query='select * from CHARACTERS'
cur.execute(query)
characters=cur.fetchall()

query = "select * from STEPS"
cur.execute(query)
stepaventure = cur.fetchall()


query = "select * from OPTIONS"
cur.execute(query)
optionaventure = cur.fetchall()

userplayrecord=['No records archieved']

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


def menu_options_loged(opc,userplayrecord):
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
                print('Id Adventure       ', 'Adventure', ' ' * 40, 'Description')
                print('*' * 152)
                # adventure1
                print()
                print('1', ' ' * 17, nomhis_descpcion[1][0], ' ' * 29,)
                #
                n = 80  # posicion final
                r = 0  # posicon inicial
                #
                listatexto = []
                while n < len(desadven1):
                    j = 0
                    while desadven1[n] != ' ':
                        n = n - 1
                        j = j + 1
                    t = desadven1[r:n]
                    listatexto.append(t)
                    r = r + (80 - j)
                    n = n + (80)
                if n > len(desadven1):
                    t = desadven1[r:len(desadven1) + 1]
                    listatexto.append(t)

                for i in listatexto:
                    print(i.rjust(150))
                # adventure1
                # adventure2
                print()
                print('2', ' ' * 17, nomhis_descpcion[0][0], ' ' * 29, )
                #
                n = 80  # posicion final
                r = 0  # posicon inicial
                #
                listatexto2 = []
                while n < len(nomhis_descpcion[0][1]):
                    j = 0
                    while nomhis_descpcion[0][1][n] != ' ':
                        n = n - 1
                        j = j + 1
                    t = nomhis_descpcion[0][1][r:n]
                    listatexto2.append(t)
                    r = r + (80 - j)
                    n = n + (80)
                if n > len(nomhis_descpcion[0][1]):
                    t = nomhis_descpcion[0][1][r:len(nomhis_descpcion[0][1]) + 1]
                    listatexto2.append(t)

                for i in listatexto2:
                    print(i.rjust(150))

                # adventure2
                whichplay = input("Choose a adventure to play(0 to go back)")
                whichplay=str(whichplay)
                if whichplay == '0':
                    opc = menuloged()
                    break
                #
                pased = True
                if whichplay.isdigit()==False:
                    input('**********Invalid option**********\n\n Press enter to continue')
                    pased=False
                if pased == True:
                    if int(whichplay)<0 or int(whichplay)>2:
                        input('**********Invalid option**********\n\n Press enter to continue')
                        pased=False
                if pased==True:
                #
                    print('=' * 70, 'Characters', '=' * 70)
                    #
                    j=0
                    for i in characters:
                        j=j+1
                        print(j,') ',i[1])
                    #
                    choose_character = input('Choose a Character')
                    #
                    pased = True
                    if choose_character.isdigit() == False:
                        input('**********Invalid option**********\n\n Press enter to continue')
                        pased = False
                    if pased == True:
                        if int(choose_character) < 0 or int(choose_character) > 3:
                            input('**********Invalid option**********\n\n Press enter to continue')
                            pased = False
                    if pased == True:

                        if str(whichplay)=='2':
                            while True:#1:
                                opcrecord=[]
                                steprecord=[]
                                print('')
                                print(stepaventure[0][1],'\n ')
                                print(optionaventure[0][0],')',optionaventure[0][1])
                                print(optionaventure[1][0],')',optionaventure[1][1])
                                print(optionaventure[2][0],')',optionaventure[2][1])
                                opc1=input("Choose a option")
                                #
                                pased = True
                                if opc1.isdigit() == False:
                                    input('**********Invalid option**********\n\n Press enter to continue')
                                    pased = False
                                if pased == True:
                                    if int(opc1) < 1 or int(opc1) > 3:
                                        input('**********Invalid option**********\n\n Press enter to continue')
                                        pased = False
                                if pased == True:
                                    if str(opc1)=='1':
                                        while True:#1.1,2:
                                            opcrecord.append(optionaventure[0][0])
                                            steprecord.append(stepaventure[0][0])
                                            print('')
                                            print(optionaventure[0][2])
                                            print(stepaventure[1][1], '\n ')
                                            print('1 )', optionaventure[3][1])
                                            print('2 )', optionaventure[4][1])
                                            print('3 )', optionaventure[6][1])
                                            opc2 = input("Choose a option")
                                            #
                                            pased = True
                                            if opc2.isdigit() == False:
                                                input('**********Invalid option**********\n\n Press enter to continue')
                                                pased = False
                                            if pased == True:
                                                if int(opc2) < 1 or int(opc2) > 3:
                                                    input('**********Invalid option**********\n\n Press enter to continue')
                                                    pased = False
                                            if pased == True:
                                                if str(opc2) == '1':
                                                    while True:#1.1,2.4,3:
                                                        opcrecord.append(optionaventure[3][0])
                                                        steprecord.append(stepaventure[1][0])
                                                        print('')
                                                        print(optionaventure[3][2])
                                                        print(stepaventure[2][1], '\n ')
                                                        print('1 )', optionaventure[7][1])
                                                        print('2 )', optionaventure[8][1])
                                                        opc3 = input("Choose a option")
                                                        #
                                                        pased = True
                                                        if opc3.isdigit() == False:
                                                            input(
                                                                '**********Invalid option**********\n\n Press enter to continue')
                                                            pased = False
                                                        if pased == True:
                                                            if int(opc3) < 1 or int(opc3) > 2:
                                                                input(
                                                                    '**********Invalid option**********\n\n Press enter to continue')
                                                                pased = False
                                                        if pased == True:
                                                            #end 1.1,2.4,3.8
                                                            if str(opc3)=='1':
                                                                opcrecord.append( optionaventure[7][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[7][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                            elif str(opc3)=='2':
                                                                opcrecord.append( optionaventure[8][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[8][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '2':
                                                    while True:#1.1,2.5,3:
                                                        opcrecord.append(optionaventure[4][0])
                                                        steprecord.append(stepaventure[1][0])
                                                        print('')
                                                        print(optionaventure[4][2])
                                                        print(stepaventure[2][1], '\n ')
                                                        print('1 )', optionaventure[7][1])
                                                        print('2 )', optionaventure[8][1])
                                                        opc3 = input("Choose a option")
                                                        #
                                                        pased = True
                                                        if opc3.isdigit() == False:
                                                            input(
                                                                '**********Invalid option**********\n\n Press enter to continue')
                                                            pased = False
                                                        if pased == True:
                                                            if int(opc3) < 1 or int(opc3) > 2:
                                                                input(
                                                                    '**********Invalid option**********\n\n Press enter to continue')
                                                                pased = False
                                                        if pased == True:
                                                            #end 1.1,2.4,3.8
                                                            if str(opc3) == '1':
                                                                opcrecord.append(optionaventure[7][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[7][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                            elif str(opc3) == '2':
                                                                opcrecord.append(optionaventure[8][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[8][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '3':
                                                    while True:#end 1.1,2.7:
                                                        opcrecord.append(optionaventure[6][0])
                                                        steprecord.append(stepaventure[1][0])
                                                        print(optionaventure[6][2])
                                                        print('THE END')
                                                        from datetime import datetime
                                                        now = datetime.now()
                                                        userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                        return userplayrecord, 'nivel-completado'
                                    elif str(opc1)=='2':
                                        while True:#1.2,2:
                                            opcrecord.append(optionaventure[1][0])
                                            steprecord.append(stepaventure[0][0])
                                            print('')
                                            print(optionaventure[1][2])
                                            print(stepaventure[1][1], '\n ')
                                            print('1 )', optionaventure[3][1])
                                            print('2 )', optionaventure[4][1])
                                            print('3 )', optionaventure[6][1])
                                            opc2 = input("Choose a option")
                                            #
                                            pased = True
                                            if opc2.isdigit() == False:
                                                input('**********Invalid option**********\n\n Press enter to continue')
                                                pased = False
                                            if pased == True:
                                                if int(opc2) < 1 or int(opc2) > 3:
                                                    input('**********Invalid option**********\n\n Press enter to continue')
                                                    pased = False
                                            if pased == True:
                                                if str(opc2) == '1':
                                                    while True:#1.1,2.4,3:
                                                        opcrecord.append(optionaventure[3][0])
                                                        steprecord.append(stepaventure[1][0])
                                                        print('')
                                                        print(optionaventure[3][2])
                                                        print(stepaventure[2][1], '\n ')
                                                        print('1 )', optionaventure[7][1])
                                                        print('2 )', optionaventure[8][1])
                                                        opc3 = input("Choose a option")
                                                        #
                                                        pased = True
                                                        if opc3.isdigit() == False:
                                                            input(
                                                                '**********Invalid option**********\n\n Press enter to continue')
                                                            pased = False
                                                        if pased == True:
                                                            if int(opc3) < 1 or int(opc3) > 2:
                                                                input(
                                                                    '**********Invalid option**********\n\n Press enter to continue')
                                                                pased = False
                                                        if pased == True:
                                                            #end 1.1,2.4,3.8
                                                            if str(opc3)=='1':
                                                                opcrecord.append( optionaventure[7][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[7][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                            elif str(opc3)=='2':
                                                                opcrecord.append( optionaventure[8][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[8][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '2':
                                                    while True:#1.1,2.5,3:
                                                        opcrecord.append(optionaventure[4][0])
                                                        steprecord.append(stepaventure[1][0])
                                                        print('')
                                                        print(optionaventure[4][2])
                                                        print(stepaventure[2][1], '\n ')
                                                        print('1 )', optionaventure[7][1])
                                                        print('2 )', optionaventure[8][1])
                                                        opc3 = input("Choose a option")
                                                        #
                                                        pased = True
                                                        if opc3.isdigit() == False:
                                                            input(
                                                                '**********Invalid option**********\n\n Press enter to continue')
                                                            pased = False
                                                        if pased == True:
                                                            if int(opc3) < 1 or int(opc3) > 2:
                                                                input(
                                                                    '**********Invalid option**********\n\n Press enter to continue')
                                                                pased = False
                                                        if pased == True:
                                                            #end 1.1,2.4,3.8
                                                            if str(opc3) == '1':
                                                                opcrecord.append(optionaventure[7][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[7][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                            elif str(opc3) == '2':
                                                                opcrecord.append(optionaventure[8][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[8][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '3':
                                                    while True:#end 1.1,2.7:
                                                        opcrecord.append(optionaventure[6][0])
                                                        steprecord.append(stepaventure[1][0])
                                                        print(optionaventure[6][2])
                                                        print('THE END')
                                                        from datetime import datetime
                                                        now = datetime.now()
                                                        userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                        return userplayrecord, 'nivel-completado'
                                    elif str(opc1)=='3':
                                        while True:#1.2,2:
                                            opcrecord.append(optionaventure[2][0])
                                            steprecord.append(stepaventure[0][0])
                                            print('')
                                            print(optionaventure[2][2])
                                            print(stepaventure[1][1], '\n ')
                                            print('1 )', optionaventure[3][1])
                                            print('2 )', optionaventure[4][1])
                                            print('3 )', optionaventure[6][1])
                                            opc2 = input("Choose a option")
                                            #
                                            pased = True
                                            if opc2.isdigit() == False:
                                                input('**********Invalid option**********\n\n Press enter to continue')
                                                pased = False
                                            if pased == True:
                                                if int(opc2) < 1 or int(opc2) > 3:
                                                    input('**********Invalid option**********\n\n Press enter to continue')
                                                    pased = False
                                            if pased == True:
                                                if str(opc2) == '1':
                                                    while True:#1.1,2.4,3:
                                                        opcrecord.append(optionaventure[3][0])
                                                        steprecord.append(stepaventure[1][0])
                                                        print('')
                                                        print(optionaventure[3][2])
                                                        print(stepaventure[2][1], '\n ')
                                                        print('1 )', optionaventure[7][1])
                                                        print('2 )', optionaventure[8][1])
                                                        opc3 = input("Choose a option")
                                                        #
                                                        pased = True
                                                        if opc3.isdigit() == False:
                                                            input(
                                                                '**********Invalid option**********\n\n Press enter to continue')
                                                            pased = False
                                                        if pased == True:
                                                            if int(opc3) < 1 or int(opc3) > 2:
                                                                input(
                                                                    '**********Invalid option**********\n\n Press enter to continue')
                                                                pased = False
                                                        if pased == True:
                                                            #end 1.1,2.4,3.8
                                                            if str(opc3)=='1':
                                                                opcrecord.append( optionaventure[7][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[7][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                            elif str(opc3)=='2':
                                                                opcrecord.append( optionaventure[8][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[8][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '2':
                                                    while True:#1.1,2.5,3:
                                                        opcrecord.append(optionaventure[4][0])
                                                        steprecord.append(stepaventure[1][0])
                                                        print('')
                                                        print(optionaventure[4][2])
                                                        print(stepaventure[2][1], '\n ')
                                                        print('1 )', optionaventure[7][1])
                                                        print('2 )', optionaventure[8][1])
                                                        opc3 = input("Choose a option")
                                                        #
                                                        pased = True
                                                        if opc3.isdigit() == False:
                                                            input(
                                                                '**********Invalid option**********\n\n Press enter to continue')
                                                            pased = False
                                                        if pased == True:
                                                            if int(opc3) < 1 or int(opc3) > 2:
                                                                input(
                                                                    '**********Invalid option**********\n\n Press enter to continue')
                                                                pased = False
                                                        if pased == True:
                                                            #end 1.1,2.4,3.8
                                                            if str(opc3) == '1':
                                                                opcrecord.append(optionaventure[7][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[7][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                            elif str(opc3) == '2':
                                                                opcrecord.append(optionaventure[8][0])
                                                                steprecord.append(stepaventure[2][0])
                                                                print(optionaventure[8][2])
                                                                print('THE END')
                                                                from datetime import datetime
                                                                now = datetime.now()
                                                                userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                                return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '3':
                                                    while True:#end 1.1,2.7:
                                                        opcrecord.append(optionaventure[6][0])
                                                        steprecord.append(stepaventure[1][0])
                                                        print(optionaventure[6][2])
                                                        print('THE END')
                                                        from datetime import datetime
                                                        now = datetime.now()
                                                        userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                        return userplayrecord, 'nivel-completado'

                        elif str(whichplay)=='1':
                            while True:  # 1:
                                opcrecord = []
                                steprecord = []
                                print('')
                                print(stepaventure[5][1], '\n ')
                                print('1 )', optionaventure[9][1])
                                print('2 )', optionaventure[10][1])
                                print('3 )', optionaventure[11][1])
                                opc1 = input("Choose a option")
                                #
                                pased = True
                                if opc1.isdigit() == False:
                                    input('**********Invalid option**********\n\n Press enter to continue')
                                    pased = False
                                if pased == True:
                                    if int(opc1) < 1 or int(opc1) > 3:
                                        input('**********Invalid option**********\n\n Press enter to continue')
                                        pased = False
                                if pased == True:
                                    if str(opc1)=='1':
                                        while True:#1.1,2:
                                            opcrecord.append(optionaventure[9][0])
                                            steprecord.append(stepaventure[5][0])
                                            print('')
                                            print(optionaventure[9][2])
                                            print(stepaventure[6][1], '\n ')
                                            print('1 )', optionaventure[12][1])
                                            print('2 )', optionaventure[13][1])
                                            print('3 )', optionaventure[14][1])
                                            opc2 = input("Choose a option")
                                            #
                                            pased = True
                                            if opc2.isdigit() == False:
                                                input('**********Invalid option**********\n\n Press enter to continue')
                                                pased = False
                                            if pased == True:
                                                if int(opc2) < 1 or int(opc2) > 3:
                                                    input('**********Invalid option**********\n\n Press enter to continue')
                                                    pased = False
                                            if pased == True:
                                                if str(opc2) == '1':
                                                    opcrecord.append(optionaventure[12][0])
                                                    steprecord.append(stepaventure[6][0])
                                                    print(optionaventure[12][2])
                                                    print('THE END')
                                                    from datetime import datetime
                                                    now = datetime.now()
                                                    userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                    return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '2':
                                                    opcrecord.append(optionaventure[13][0])
                                                    steprecord.append(stepaventure[6][0])
                                                    print(optionaventure[13][2])
                                                    print('THE END')
                                                    from datetime import datetime
                                                    now = datetime.now()
                                                    userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                    return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '3':
                                                    opcrecord.append(optionaventure[14][0])
                                                    steprecord.append(stepaventure[6][0])
                                                    print(optionaventure[14][2])
                                                    print('THE END')
                                                    from datetime import datetime
                                                    now = datetime.now()
                                                    userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                    return userplayrecord, 'nivel-completado'

                                    elif str(opc1)=='2':
                                        while True:#1.1,2:
                                            opcrecord.append(optionaventure[10][0])
                                            steprecord.append(stepaventure[5][0])
                                            print('')
                                            print(optionaventure[10][2])
                                            print(stepaventure[6][1], '\n ')
                                            print('1 )', optionaventure[12][1])
                                            print('2 )', optionaventure[13][1])
                                            print('3 )', optionaventure[14][1])
                                            opc2 = input("Choose a option")
                                            #
                                            pased = True
                                            if opc2.isdigit() == False:
                                                input('**********Invalid option**********\n\n Press enter to continue')
                                                pased = False
                                            if pased == True:
                                                if int(opc2) < 1 or int(opc2) > 3:
                                                    input('**********Invalid option**********\n\n Press enter to continue')
                                                    pased = False
                                            if pased == True:
                                                if str(opc2) == '1':
                                                    opcrecord.append(optionaventure[12][0])
                                                    steprecord.append(stepaventure[6][0])
                                                    print(optionaventure[12][2])
                                                    print('THE END')
                                                    from datetime import datetime
                                                    now = datetime.now()
                                                    userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                    return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '2':
                                                    opcrecord.append(optionaventure[13][0])
                                                    steprecord.append(stepaventure[6][0])
                                                    print(optionaventure[13][2])
                                                    print('THE END')
                                                    from datetime import datetime
                                                    now = datetime.now()
                                                    userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                    return userplayrecord, 'nivel-completado'
                                                elif str(opc2) == '3':
                                                    opcrecord.append(optionaventure[14][0])
                                                    steprecord.append(stepaventure[6][0])
                                                    print(optionaventure[14][2])
                                                    print('THE END')
                                                    from datetime import datetime
                                                    now = datetime.now()
                                                    userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                                    return userplayrecord, 'nivel-completado'

                                    elif str(opc1) == '3':
                                        opcrecord.append(optionaventure[11][0])
                                        steprecord.append(stepaventure[6][0])
                                        print(optionaventure[11][2])
                                        print('THE END')
                                        from datetime import datetime
                                        now = datetime.now()
                                        userplayrecord = [login1[0],choose_character,steprecord, opcrecord,now,whichplay]
                                        return userplayrecord, 'nivel-completado'

        elif opc == '3':
            if userplayrecord[0] == 'No records archieved':
                print('Replay adventure')
                print(' ' * 65)
                print('*' * 150)
                print('ID', ' ' * 22, 'USERNAME', ' ' * 22, 'NAME', ' ' * 22, 'CHARACTER NAME', ' ' * 22, 'DATE')
                print('*' * 150)
                print(userplayrecord)
                input("Press enter to exit")
                return ['None', 'None', False]
            else:
                d = getUser.getUser()
                print('Replay adventure')
                print(' ' * 65)
                for i in d:
                    if userplayrecord[0] == i:
                        userplayrecord.append(d[i]['userId'])
                if str(userplayrecord[5]) == '1':
                    userplayrecord[5] = 'Lucha contra duendes'
                if str(userplayrecord[5]) == '2':
                    userplayrecord[5] = 'Cobra kai'
                if str(userplayrecord[1]) == '1':
                    userplayrecord[1] = 'Kratos'
                if str(userplayrecord[1]) == '2':
                    userplayrecord[1] = 'cristiano ronaldo'
                if str(userplayrecord[1]) == '3':
                    userplayrecord[1] = 'ibai'

                print('*' * 150)
                print('ID', ' ' * 22, 'USERNAME', ' ' * 22, 'NAME', ' ' * 22, 'CHARACTER NAME', ' ' * 22, 'DATE')
                print('*' * 150)
                print(userplayrecord[6], ' ' * 23, userplayrecord[0], ' ' * 23, userplayrecord[5], ' ' * 6,
                      userplayrecord[1], ' ' * 15, userplayrecord[4])
                input("Press enter to exit")
                return ['None', 'None', False]
        elif opc == '4':
            if userplayrecord[0] == 'No records archieved':
                print('Replay adventure')
                print(' ' * 65)
                print('*' * 150)
                print('ID', ' ' * 22, 'USERNAME', ' ' * 22, 'NAME', ' ' * 22, 'CHARACTER NAME', ' ' * 22, 'DATE')
                print('*' * 150)
                print(userplayrecord)
                input("Press enter to exit")
                return ['None', 'None', False]
            else:
                d = getUser.getUser()
                print('Replay adventure')
                print(' ' * 65)
                for i in d:
                    if userplayrecord[0] == i:
                        userplayrecord.append(d[i]['userId'])
                if str(userplayrecord[5]) == '1':
                    userplayrecord[5] = 'Lucha contra duendes'
                if str(userplayrecord[5]) == '2':
                    userplayrecord[5] = 'Cobra kai'
                if str(userplayrecord[1]) == '1':
                    userplayrecord[1] = 'Kratos'
                if str(userplayrecord[1]) == '2':
                    userplayrecord[1] = 'cristiano ronaldo'
                if str(userplayrecord[1]) == '3':
                    userplayrecord[1] = 'ibai'

                print('*' * 150)
                print('ID', ' ' * 22, 'USERNAME', ' ' * 22, 'NAME', ' ' * 22, 'CHARACTER NAME', ' ' * 22, 'DATE')
                print('*' * 150)
                print(userplayrecord[6], ' ' * 23, userplayrecord[0], ' ' * 23, userplayrecord[5], ' ' * 6,
                      userplayrecord[1], ' ' * 15, userplayrecord[4])
                input("Press enter to exit")
                return ['None', 'None', False]
        elif opc == '5':
            return 'exit'


def menu_options(opc,userplayrecord):
    if opc == '1':
        while True:
            user = input('Input username: ')
            d = getUser.getUser()
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
                                login1=['None', 'None', False]
                                return login1
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
        if userplayrecord[0] == 'No records archieved':
            print('Replay adventure')
            print(' ' * 65)
            print('*' * 150)
            print('ID', ' ' * 22, 'USERNAME', ' ' * 22, 'NAME', ' ' * 22, 'CHARACTER NAME', ' ' * 22, 'DATE')
            print('*' * 150)
            print(userplayrecord)
            input("Press enter to exit")
            return ['None', 'None', False]
        else:
            d = getUser.getUser()
            print('Replay adventure')
            print(' ' * 65)
            for i in d:
                if userplayrecord[0] == i:
                    userplayrecord.append(d[i]['userId'])
            if str(userplayrecord[5]) == '1':
                userplayrecord[5] = 'Lucha contra duendes'
            if str(userplayrecord[5]) == '2':
                userplayrecord[5] = 'Cobra kai'
            if str(userplayrecord[1]) == '1':
                userplayrecord[1] = 'Kratos'
            if str(userplayrecord[1]) == '2':
                userplayrecord[1] = 'cristiano ronaldo'
            if str(userplayrecord[1]) == '3':
                userplayrecord[1] = 'ibai'

            print('*' * 150)
            print('ID', ' ' * 22, 'USERNAME', ' ' * 22, 'NAME', ' ' * 22, 'CHARACTER NAME', ' ' * 22, 'DATE')
            print('*' * 150)
            print(userplayrecord[6], ' ' * 23, userplayrecord[0], ' ' * 23, userplayrecord[5], ' ' * 6,
                  userplayrecord[1], ' ' * 15, userplayrecord[4])
            input("Press enter to exit")
            return ['None','None',False]
    elif opc == '4':
        if userplayrecord[0] == 'No records archieved':
            print('Replay adventure')
            print(' ' * 65)
            print('*' * 150)
            print('ID', ' ' * 22, 'USERNAME', ' ' * 22, 'NAME', ' ' * 22, 'CHARACTER NAME', ' ' * 22, 'DATE')
            print('*' * 150)
            print(userplayrecord)
            input("Press enter to exit")
            return ['None', 'None', False]
        else:
            d = getUser.getUser()
            print('Replay adventure')
            print(' ' * 65)
            for i in d:
                if userplayrecord[0] == i:
                    userplayrecord.append(d[i]['userId'])
            if str(userplayrecord[5]) == '1':
                userplayrecord[5] = 'Lucha contra duendes'
            if str(userplayrecord[5]) == '2':
                userplayrecord[5] = 'Cobra kai'
            if str(userplayrecord[1]) == '1':
                userplayrecord[1] = 'Kratos'
            if str(userplayrecord[1]) == '2':
                userplayrecord[1] = 'cristiano ronaldo'
            if str(userplayrecord[1]) == '3':
                userplayrecord[1] = 'ibai'

            print('*' * 150)
            print('ID', ' ' * 22, 'USERNAME', ' ' * 22, 'NAME', ' ' * 22, 'CHARACTER NAME', ' ' * 22, 'DATE')
            print('*' * 150)
            print(userplayrecord[6], ' ' * 23, userplayrecord[0], ' ' * 23, userplayrecord[5], ' ' * 6,
                  userplayrecord[1], ' ' * 15, userplayrecord[4])
            input("Press enter to exit")
            return ['None', 'None', False]
    elif opc == '5':
        exit1 = 'exit'
        return exit1


while True:
    login1 = menu_options(menunologin(),userplayrecord)
    if login1 == 'exit':
        print("BYE")
        break
    print(1)
    if login1[2] == True:
        while True:
            if login1[2] == True:
                login2 = menu_options_loged(menuloged(),userplayrecord)
                if login2 == 'logout':
                    break
                elif login2[1] == 'nivel-completado':
                    userplayrecord=login2[0]
                    #Falta para guardar este userplayrecord en bbdd
                    input("Press enter to continue")
                elif login2 == 'exit':
                    login1 = 'exit'
                    break
